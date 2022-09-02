from main import app, db
from flask import request, redirect, render_template, url_for, flash
from methods import extrair_html, extrair_dados,verifica_url
from models import Artigo


@app.route("/", methods=['GET'])
def index():
    artigo = Artigo.query.all()
    return render_template('index.html', tamanho_lista=len(artigo), lista_de_artigos= artigo)


@app.route("/adicionar", methods=['POST'])
def adicionar():
    titulo= request.form['titulo']
    link = request.form['link']
    if (Artigo.query.filter_by(titulo=titulo).first()):
        flash('Artigo já existente!')
        return redirect(url_for("index"))
    else:
        artigo = Artigo(titulo, link)
        db.session.add(artigo)
        db.session.commit()
        flash('Artigo adicionado!')
        return redirect(url_for("index"))


@app.route("/delete/<int:id_artigo>",  methods=['GET', 'POST'])
def delete(id_artigo):
    artigo = Artigo.query.filter_by(id_artigo=id_artigo).first()
    db.session.delete(artigo)
    db.session.commit()
    flash('Artigo removido!')
    return redirect(url_for("index"))


@app.route("/atualizar/<int:id_artigo>",  methods=['GET', 'POST'])
def atualizar(id_artigo):
    if(request.method == 'GET'):
        artigo = Artigo.query.filter_by(id_artigo=id_artigo).first()
        return render_template('atualizar.html', artigo=artigo)
    else:
        pass


@app.route("/atualizar_dados/<int:id_artigo>",  methods=['POST'])
def atualizar_dados(id_artigo):
    artigo = Artigo.query.filter_by(id_artigo=id_artigo).first()
    if(request.method == 'POST'):
        artigo.titulo = request.form['titulo']
        artigo.link = request.form['link']
        db.session.commit()
        flash('Artigo atualizado!')
        return redirect(url_for("index"))


@app.route("/importar", methods=['GET'])
def importar():
    return render_template('importar.html')


@app.route("/extrair_links", methods=['POST'])
def extrair_links():
    link = request.form['extrair_link']
    url_valida = verifica_url(link)
    if url_valida == 0 or url_valida == 1:
        html = extrair_html(link)
        extrair_dados(html, url_valida)
        flash('Artigos importados')
        return redirect(url_for('index'))
    else:
        flash('Link invalido para importar!')
        return redirect(url_for('index'))