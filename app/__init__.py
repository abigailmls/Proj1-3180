from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os.path import join,dirname,realpath


SECRET_KEY = 'Sup3r$3cretkey'

app = Flask(__name__)

app.config['SECRET_KEY'] = '\xee\xca\xb9.Q\xf7\xbd\xfe\xda|X\xfb\x93\x98\xdc\x15\x15(\x13z#D\xef\x1a\xb3'
app.config['SQLALCHEMY_DATABASE_URI'] ="postgres://project:pass1@localhost/projectdb"
#Heroku Daatabase
app.config['SQLALCHEMY_DATABASE_URI']="postgres://rxbfjjcyurzsol:bd1a7bab64ffef15e6d9503442f4ca96b4f2802b3be9f2cbfd65e844ff055a53@ec2-18-215-99-63.compute-1.amazonaws.com:5432/d4uhg8smjsg5bu"
#app.config['UPLOAD_FOLDER']= join(dirname(realpath(__file__)), 'static/uploads')


app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True 

db = SQLAlchemy(app)

app.config.from_object(__name__)


from app import views
