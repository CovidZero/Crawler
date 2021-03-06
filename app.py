#!/usr/bin/env python
# coding: utf-8
# In[12]:

import urllib3
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import datetime
import os
import subprocess as cmd
import argparse
from config import BUCKET_NAME, LINKS_REPO, PROG_NAME, VERSION, PASTA_RESULTADO, REPO_URL, ESTADOS
import sys
import boto3
import aiohttp
import asyncio
import time

#Projeto https://covidzero.com.br/

SITES_COM_PROBLEMAS = []
SITES_VERIFICADOS = []
start_time = time.time()

def LerArquivo(subdiretorio):
    x = datetime.datetime.now()
    data = x.strftime("%Y%m%d")
    arq = open(subdiretorio,'r', encoding='utf-8')
    #print(arq.read())
    lista = []
    for item in arq:
        #print(item)
        lista.append(str(item).strip())
    print(lista)
    arq.close()
    return lista

def gravarNoArquivoUrl(n1,n2,diretorio):
    x = datetime.datetime.now()
    data = x.strftime('%d-%m-%Y_%H')
    create_directory(diretorio) 
    arquivo = open(diretorio+'\\covidZero_resultado_'+ data+'.csv', 'a',encoding='utf-8')
    arquivo.write('%s;%s\n' %(n1,n2))
    arquivo.flush()
    arquivo.close()

def create_directory(dirName):
    if not os.path.exists(dirName):
        os.makedirs(dirName)

async def fetch(pagina, novas_paginas, diretorio, estado):
    async with aiohttp.ClientSession() as session:
        async with session.get(pagina) as resp:
            if (resp.status == 200 and ('text/html' in resp.headers.get('content-type'))):
                data = (await resp.read()).decode('utf-8', 'replace')
                SITES_VERIFICADOS.append(pagina)
                return varrendo_pagina(data, pagina, novas_paginas, diretorio, estado)                  

def varrendo_pagina(data, pagina, novas_paginas, diretorio, estado):
    sopa = BeautifulSoup(data,'lxml')
    print('\n**** Crawling noticias de {} ******\n'.format(estado))
    print('Url utilizada {}'.format(pagina))
    bolsolinks = set()
    links = sopa.find_all('a')
    contador = 1
    for link in links:

        if ('title' in link.attrs):
            title = str(link.get('title').lower())
            url = urljoin(pagina, str(link.get('href')))

            if title.__contains__('coronavirus') or title.__contains__('COVID-19') or title.__contains__('covid'):
                if url[-1] == '/':
                    tamanho = len(url)
                    url = url[:tamanho-1]
                bolsolinks.add(url)

        if ('href' in link.attrs):
            url = urljoin(pagina, str(link.get('href')))                    

            if url.find("'") != -1:
                continue                    

            url = url.split('#')[0]
            
            if url[0:4] == 'http' or url[0:5] == 'https':
                novas_paginas.add(url)
                if url.__contains__('coronavirus') or url.__contains__('COVID-19') or url.__contains__('covid'):
                    if url[-1] == '/':
                        tamanho = len(url)
                        url = url[:tamanho-1]
                    bolsolinks.add(url)

        contador = contador + 1

    for bolso in bolsolinks:
        gravarNoArquivoUrl(pagina,bolso,diretorio)          

async def crawl(estado, paginas, profundidade, diretorio):   
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    for i in range(profundidade):
        novas_paginas = set()
        for pagina in paginas:
            try:
                await fetch(pagina, novas_paginas, diretorio, estado)
            except Exception as exc:
                print('Erro ao abrir a página ' + pagina)
                print (exc)
                SITES_COM_PROBLEMAS.append(pagina)
                continue
            
def parse_argumentos(args):
    formatter_class = argparse.RawDescriptionHelpFormatter
    parser = argparse.ArgumentParser(prog=PROG_NAME,formatter_class=formatter_class)

    parser.add_argument("--version", action="version", version="%(prog)s {}".format(VERSION))
    parser.add_argument('--salvar', action='store_true', default=False,
                        help="Indica se o resultado da execução deve ser salvo no respositorio de Arquivos")
    parser.add_argument('--salvars3', action='store_true', default=False,
                        help="Indica se o resultado da execução deve ser salvo no respositorio de Arquivos") #Refatorar para o salvar ser uma lista de opções
    parser.add_argument('--links', action='store', default=PASTA_RESULTADO,
                        help="define o caminho para carregar os links por estado")

    return parser.parse_args(args)

def salvar_resultado(url):
    #Importante adicionar [O upstream]  git remote add upstream {reposiorio de Arquivos}
    #Commit no Git upstream
    cp = cmd.run("git remote add upstream {}".format(url), check=True, shell=True)
    cp = cmd.run("git init", check=True, shell=True)
    cp = cmd.run("git add Estados", check=True, shell=True)
    cp = cmd.run(f'git commit -m "Atualizando"', check=True, shell=True)
    cp = cmd.run(f"git push upstream master -f", check=True, shell=True)

def get_url_estado(estado):
    return LINKS_REPO.format(estado)

def salvar_no_S3(caminho_arquivos):
    try:
        s3_resource = boto3.resource('s3')
        for root, estados, arquivos in os.walk(caminho_arquivos, topdown=True):
            for arquivo in arquivos:
                (base, ext) = os.path.splitext(arquivo)
                if ext == '.csv':
                    nome_arquivo = os.path.join(root, arquivo)
                    key = os.path.join(root.replace('.', ''), arquivo).replace('\\', '/')[1:]
                    print ("Salvando arquivo {} no S3".format(nome_arquivo))
                    s3_resource.Bucket(BUCKET_NAME).upload_file(Filename=nome_arquivo, Key=key)
                    os.remove(nome_arquivo)
    except Exception as exc:
        print("Erro ao salvar no S3")
        print(exc) 

def get_sites_por_estado(url_estado, estado):
    print('Buscando urls para o estado {}'.format(estado))
    http = urllib3.PoolManager()
    r = http.request('GET', url_estado)

    if (r.status == 200):
        return str(r.data.decode('utf-8')).split('\n')

def executa_crawler(args):
    path = args.links
    tasks = []
    loop = asyncio.get_event_loop()
    for estado in ESTADOS:
        url = get_url_estado(estado)
        sites = get_sites_por_estado(url, estado)
        pathSub = path + '\\'+ estado 
        tasks.append(loop.create_task(crawl(estado, sites, 1, pathSub)))

    loop.run_until_complete(asyncio.wait(tasks)) 
    
    print('Lista de sites com problemas')
    print('\n'.join(map(str, SITES_COM_PROBLEMAS)))

    print('*** Total de sites com verificados {}'.format(len(SITES_VERIFICADOS)))
    print('*** Total de sites com problemas {}'.format(len(SITES_COM_PROBLEMAS)))
            
if __name__ == '__main__':
    ##Obs se for necessario podemos fazer pela rede tor, para nao entrarmos na black list dos sites
    try:
        print('*** iniciando processo de crawler noticias...\n')
        args = arguments = parse_argumentos(sys.argv[1:])
        executa_crawler(args)    
        
        if (args.salvars3):
            salvar_no_S3(PASTA_RESULTADO)
        
        if (args.salvar):
            salvar_resultado(REPO_URL)

        tempo_total = (time.time() - start_time) / 60
        print('*** Tempo total de execução {:d} minutos'.format(int(tempo_total)))

    except Exception as exc:
        print(exc)
    