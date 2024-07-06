# CRIAR A ESTRUTURA DO BANCO DE DADOS
from fakepinterest import db, login_manager
from flask import url_for
from datetime import datetime
from flask_login import UserMixin
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import ForeignKey, Integer, String,column
import os
from werkzeug.utils import secure_filename


@login_manager.user_loader
def load_usuario(id_usuario):
    return Usuario.query.get(int(id_usuario))

class Usuario(db.Model, UserMixin):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(nullable=False)
    email: Mapped[str] = mapped_column(nullable=False, unique=True)
    senha: Mapped[str] = mapped_column(nullable=False)
    fotos: Mapped["Foto"] = relationship(backref="usuario", lazy=True)

   

class Foto(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    imagem: Mapped[str] = mapped_column(nullable=False, default='default.png')
    data_criacao: Mapped[datetime] = mapped_column(nullable=False, default=datetime.utcnow)
    id_usuario: Mapped[int] = mapped_column(ForeignKey("usuario.id"), nullable=False)    

   