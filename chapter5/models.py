from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.INTEGER, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(80), nullable=False)


class CodeCountRecord(db.Model):
    __tablename = 'codecountrecord'
    id = db.Column(db.INTEGER, primary_key=True)
    count = db.Column(db.INTEGER)
    data = db.Column(db.DATE)
    user = db.Column(db.ForeignKey('user.id'))


db.create_all()
