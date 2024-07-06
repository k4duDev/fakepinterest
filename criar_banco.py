# criar banco de dados
from fakepinterest import db, app
from fakepinterest.models import Usuario, Foto

with app.app_context():
    db.drop_all()
    db.create_all()