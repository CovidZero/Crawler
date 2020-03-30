#!/usr/bin/env python
# coding: utf-8
import os

PROG_NAME = 'Crawler_COVID'
VERSION = '1.0.0.0'
PASTA_RESULTADO = '.\Estados'
REPO_URL = 'https://github.com/CovidZeroNews/Arquivo.git'

LINKS_REPO = 'https://raw.githubusercontent.com/CovidZeroNews/Arquivo/master/Estados/{}/lista_sites.txt'

ESTADOS = ['AC', 'AL', 'AM', 'AP', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MG', 'MS', 'MT',
            'PA', 'PB', 'PE', 'PI', 'PR', 'RJ', 'RN', 'RO', 'RR', 'RS', 'SC', 'SE', 'SP', 'TO']

BUCKET_RESULTADO = 'crawler-noticias'

#precisa passar
#AWS_ACCESS_KEY_ID
#AWS_SECRET_ACCESS_KEY