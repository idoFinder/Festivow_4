from flask import Flask
from flask_sqlalchemy import SQLAlchemy



# creating the connection engine
app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
# mysql://username:password@server/db
engine = app.config['SQLALCHEMY_DATABASE_URI'] ='mysql://root:150492@localhost/festivow'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)



# users table
class Users(db.Model):
    __tablename__ = 'users'
    # id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.Unicode)
    email = db.Column('email', db.Unicode, primary_key=True)
    password = db.Column('password', db.Unicode)

    def __init__(self, name, email, password):
        # self.id = id
        self.name = name
        self.email = email
        self.password = password


# shows table
class Shows(db.Model):
    __tablename__ = 'shows'
    id = db.Column('id', db.Integer, primary_key=True)
    artist_name = db.Column('artist_name', db.Unicode)
    location = db.Column('location', db.Unicode)
    date = db.Column('date', db.Unicode)
    price = db.Column('price', db.Integer)

    def __init__(self, artist_name, location, date, price):
        self.artist_name = artist_name
        self.location = location
        self.date = date
        self.price = price









