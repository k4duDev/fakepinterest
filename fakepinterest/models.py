# CRIAR A ESTRUTURA DO BANCO DE DADOS
from fakepinterest import app, database, login_manager
from datetime import datetime
from flask_login import UserMixin
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Integer, String
import os
from werkzeug.utils import secure_filename

# class User(db.Model):
#     id: Mapped[int] = mapped_column(primary_key=True)
#     username: Mapped[str] = mapped_column(unique=True)
#     email: Mapped[str]


@login_manager.user_loader
def load_usuario(id_usuario):
    return Usuario.query.get(int(id_usuario))

class Usuario(database.Model, UserMixin):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=False, unique=True)
    senha: Mapped[str] = mapped_column(nullable=False)
    fotos: Mapped["Foto"] = relationship(backref="usuario", lazy=True)

    # id = database.column(database.Integer, primary_key=True)
    # username = database.column(database.String, nullable=False)
    # email = database.column(database.String, nullable=False, unique=True)
    # senha = database.column(database.String, nullable=False)
    # fotos = database.relationship("Foto", backref="usuario", lazy=True)


class Foto(database.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    imagem: Mapped[str] = mapped_column(nullable=False, default=('static/fotos_posts/default.png'))
    data_criacao: Mapped[datetime] = mapped_column(nullable=False, default=datetime.utcnow())
    id_usuario: Mapped[int] = mapped_column(ForeignKey("usuario.id"), nullable=False)    

    # id = database.column(database.Integer, primary_key=True)
    # imagem = database.column(database.String, default="default.png")
    # data_criacao = database.column(database.DateTime, nullable=False, default=datetime.utcnow())
    # id_usuario = database.column(database.Integer, database.ForeingKey('usuario.id'), nullable=False)