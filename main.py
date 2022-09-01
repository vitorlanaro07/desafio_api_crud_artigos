from flask import Flask, render_template, redirect, jsonify, session, url_for, request
import requests
from flask_sqlalchemy import SQLAlchemy
from html import parser
from bs4 import BeautifulSoup


app = Flask(__name__)

lista = []

class Artigo:
    def __init__(self, titulo, url):
        self.titulo = titulo
        self.url = url



@app.route("/", methods=['GET'])
def index():
    if request.method == 'GET':
        print(len(lista))
        return render_template('index.html', tamanho_lista=len(lista), lista_de_artigos= lista)

@app.route("/adicionar", methods=['POST'])
def adicionar():
    if request.method == 'POST':
        titulo= request.form['titulo']
        url = request.form['url']
        print(titulo, url)
        lista.append(Artigo(titulo, url))
        return redirect(url_for("index"))

@app.route("/importar", methods=['GET'])
def importar():
    return render_template('importar.html')


def extrair_html(url):
    sessao = requests.session()
    html = sessao.get(url).text
    return html


@app.route("/extrair_links", methods=['POST'])
def extrair_links():
    url = request.form['extrair_url']
    html = extrair_html(url)
    extrair_dados(html, url)
    return redirect(url_for('index'))


def extrair_dados(html, url):
    soup = BeautifulSoup(html, 'html.parser')
    soup.select('h1,h2')
    for item in soup.find_all('div', 'item-details'):
        link = url + item.a['href']
        titulo = item.a.text
        lista.append(Artigo(titulo, link))




if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=5000)