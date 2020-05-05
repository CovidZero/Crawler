<h1 align="center">Bem-vindo ao Crawler 📰🔍👋</h1>
<p>
  <a href="https://www.apache.org/licenses/LICENSE-2.0" target="_blank">
    <img alt="License: Apache--2.0" src="https://img.shields.io/badge/License-Apache--2.0-yellow.svg" />
  </a>
</p>
> Crawler de notícias relacionado ao COVID-19
# PROJETO ARQUIVADO E FORA DE UTILIZAÇÃO

## Pré-requisitos
- 1 - Ambiente Windows, Linux ou Mac
- 2 - [Python3](https://www.python.org/downloads/)

para baixar o projeto utilizando o git, rode o comando abaixo:

```git
git clone -b crawler_sites https://github.com/CovidZero/Crawler.git
```
## Instalando as bibliotecas necessarias

```python
pip install -r requirements.txt
```

## Usage

```
python app.py --salvar (Salvando no Git)
```
```
python app.py --salvars3 (Salvando no S3)
```
#### OBS
Para que os arquivos .csv sejam salvos no S3 você precisa:

- Definir o nome do bucket na variavel `BUCKET_NAME` do arquivo `config.py`
- Definir as variaveis de ambiente `AWS_ACCESS_KEY_ID` e `AWS_SECRET_ACCESS_KEY` com uma credential que tenha permissão de leitura e escrita de objetos no bucket

## Docker Usage

[Install Docker](https://docs.docker.com/install/)

[Install Docker Compose](https://docs.docker.com/compose/install/)

```
docker-compose build
docker-compose up -d
```

See os logs

```docker
docker logs -f [container-name]
```

Stop the Crawler

```
docker-compose down 
```
***
## 🤝 Contribuidores

👤 **Vinicius Rodrigues**

* Github: [@Suburbanno](https://github.com/Suburbanno)

👤 **Elder Santos**

* Github: [@eldersantos](https://github.com/eldersantos)

👤 **Jaime Ricardo**

* Github: [@jrick166fiap](https://github.com/jrick166fiap)

👤 **Thiago Fortunato**

* Github: [@thiagolsfortunato](https://github.com/thiagolsfortunato)
***
## Como contribuir?

Contribuições e solicitações de recursos são bem-vindos!<br />Sinta-se à vontade para abrir uma [issue](https://github.com/CovidZero/Crawler/issues). 

## 📝 Licença

Copyright © 2020 [CovidZero](https://github.com/CovidZero).<br />
This project is [Apache-2.0](https://www.apache.org/licenses/LICENSE-2.0) licensed.

