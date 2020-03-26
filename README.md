<div align="center">
	<img src="https://github.com/CovidZeroNews/Assets/blob/master/Images/Logo%20em%20PNG/COVID%20ZERO%20-%20Logo%20Horizontal%20-%20Covid%20Cinza@3x.png?raw=true" alt="Awesome">
	<br>
	<br>
	<hr>
</div>
<p align="center">
	<a href="https://covidzero.com.br/">Nosso Site</a>&nbsp;&nbsp;&nbsp;
	<a href="https://www.instagram.com/covidzerobrasil/">Instagram</a>&nbsp;&nbsp;&nbsp;
	<a href="https://join.slack.com/t/covidzero/shared_invite/zt-cwf9qixg-yhuPXt3TJVaBvH0Gwig8tQ">Slack</a>&nbsp;&nbsp;&nbsp;
</p>

## Pré-requisitos
- 1 - Ambiente Windows, Linux ou Mac(Python3 (Core) ou Anaconda)
- 2 - Bibliotecas Python(urllib3, bs4(BeautifulSoup), lxml
- 3 - Base de [Estados](https://github.com/CovidZeroNews/Arquivo), faça o download e mova para a pasta do Crawler

## Instalando Python ou Anaconda
- 1 - [Python3](https://www.python.org/downloads/)
- 2 - [Anaconda](https://www.anaconda.com/distribution/)

## Instalando as bibliotecas adicionais no Python
```python
pip install -r requirements.txt
```

para baixar o projeto utilizando o git, rode o comando abaixo:
```git
git clone -b crawler_sties {link repository}
```
## Funcionamento básico do projeto
- 1 - Estrutura de pastas Coletando - Estados > Arquivo lista_sites.txt - Onde vai conter os links dos sites daquela região
- 2 - Estrutura de pastas Resultado - Estados > Arquivo covidZero_resultado_dia-mês-ano_hora.csv
- 3 - Jupyter Notebook - Arquivo  CovidZero - Crawlers -v0.ipynb
- 4 - Python Core - Arquivo CovidZero_Crawlers_v0.py

#### IMPORTANTE
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

## Testando o projeto
#### Utlizando o Jupyter Notebook
Abrir o arquivo CovidZero - Crawlers -v0.ipynb e rode.

#### Utilizando python(Core)(Windows)
No cmd rode o comando abaixo:
```python
Abra o cmd e navegue até a pasta raiz do projeto
python CovidZero_Crawlers_v0.py
```
#### Utilizando python(Core)(Linux) 
rode o comando abaixo de dentro da pasta raiz do projeto:
```python
python CovidZero_Crawlers_v0.py
```

### TODO:
- [ ] O resultado(Pasta Estados) deve ser gravado no seguinte repositorio: [Arquivo](https://github.com/CovidZeroNews/Arquivo) 

### Futuras implementações e melhorias:
- [ ] Um processo que rode de tempos em tempos realizando um novo sync dos dados(Cron+ Servidor Web) (Pendente)
- [ ] Refatoração da lógica (Pendente)
- [ ] Sugestões e melhorias serão aceitos (Sempre Aberto)

> Inspiração:
[**COVIDZERO**:](http://covidzero.com.br/)
