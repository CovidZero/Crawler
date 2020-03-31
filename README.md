## Pré-requisitos
- 1 - Ambiente Windows, Linux ou Mac(Python3 (Core) ou Anaconda)
- 2 - Bibliotecas Python(urllib3, bs4(BeautifulSoup), lxml

## Instalando Python ou Anaconda
- 1 - [Python3](https://www.python.org/downloads/)
- 2 - [Anaconda](https://www.anaconda.com/distribution/)

## Instalando as bibliotecas adicionais no Python
```python
pip install -r requirements.txt
```

para baixar o projeto utilizando o git, rode o comando abaixo:
```git
git clone -b crawler_sites {link repository}
```
## Funcionamento básico do projeto
- 1 - Estrutura de pastas Coletando - Estados > Arquivo lista_sites.txt - Onde vai conter os links dos sites daquela região
- 2 - Estrutura de pastas Resultado - Estados > Arquivo covidZero_resultado_dia-mês-ano_hora.csv
- 3 - Jupyter Notebook - Arquivo  CovidZero - Crawlers -v0.ipynb
- 4 - Python Core - Arquivo CovidZero_Crawlers_v0.py


#### Salvando no Git
##### importante
- 1 - Arquivos "CovidZero - Crawlers -v0.ipynb" ou Arquivo CovidZero_Crawlers_v0.py:
- 2 - Adicione o link do seu repositório GIT de arquivos({link qui}) e descomente as linhas a abaixo:

de
```python
    #cp = cmd.run("git remote add upstream {link qui}", check=True, shell=True)
    #cp = cmd.run("git add Estados", check=True, shell=True)
    #cp = cmd.run(f'git commit -m "Atualizando"', check=True, shell=True)
    #cp = cmd.run(f"git push upstream master -f", check=True, shell=True)
```
para
```python
    cp = cmd.run("git remote add upstream {link qui}", check=True, shell=True)
    cp = cmd.run("git add Estados", check=True, shell=True)
    cp = cmd.run(f'git commit -m "Atualizando"', check=True, shell=True)
    cp = cmd.run(f"git push upstream master -f", check=True, shell=True)
```
- Executar o comando `python CovidZero_Crawlers_v0.py --salvar `

#### Salvando no S3
Para que os arquivos .csv sejam salvos no S3 você precisa:
- Definir o nome do bucket na variavel `BUCKET_RESULTADO` do arquivo `config.py`
- Definir as variaveis de ambiente `AWS_ACCESS_KEY_ID` e `AWS_SECRET_ACCESS_KEY` com uma credential que tenha permissão de leitura e escrita de objetos no bucket
- Executar o comando `python CovidZero_Crawlers_v0.py --salvars3 `

## Testando o projeto
#### Utlizando o Jupyter Notebook
Abrir o arquivo CovidZero - Crawlers -v0.ipynb e rode.

#### Utilizando Python(Core)(Windows)
No cmd rode o comando abaixo:
```python
Abra o cmd e navegue até a pasta raiz do projeto
python CovidZero_Crawlers_v0.py
```
#### Utilizando Python(Core)(Linux) 
rode o comando abaixo de dentro da pasta raiz do projeto:
```python
python CovidZero_Crawlers_v0.py
```

### Como contribuir para o projeto?
- Abra uma issue [aqui](https://github.com/CovidZeroNews/Crawler/issues) com sugestões de melhorias.

> Inspiração:
[**COVIDZERO**:](http://covidzero.com.br/)
