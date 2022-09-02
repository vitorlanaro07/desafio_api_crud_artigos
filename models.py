from main import db

class Artigo(db.Model):
    id_artigo = db.Column('id_artigo', db.Integer, primary_key=True, autoincrement=True)
    titulo = db.Column(db.String(255))
    link = db.Column(db.String(255))

    def __init__(self, titulo, link):
        self.titulo = titulo
        self.link = link