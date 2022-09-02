import requests
from bs4 import BeautifulSoup
from models import Artigo
from main import db

def extrair_html(url):
    sessao = requests.session()
    html = sessao.get(url).text
    return html


def verifica_url(url):
    if (url == 'https://tiinside.com.br/newsletter/'):
        return 0
    elif (url == 'https://devgo.com.br'):
        return 1
    else:
        return 2


def extrair_dados(html, url_valida):
    if url_valida == 0:
        extracao_dos_dados_da_pagina('div', 'item-details', html)
    else:
        extracao_dos_dados_da_pagina('h1', 'blog-article-card-title', html)


def extracao_dos_dados_da_pagina(elemento, classe, html):
    soup = BeautifulSoup(html, 'html.parser')
    for item in soup.find_all(elemento, classe):
        if elemento == 'h1':
            link = 'https://devgo.com.br' + item.a['href']
        else:
            link = item.a['href']
        titulo = item.a.text
        print(link, titulo)
        if (Artigo.query.filter_by(titulo=titulo).first()):
            pass
        else:
            artigo = Artigo(titulo, link)
            db.session.add(artigo)
            db.session.commit()


