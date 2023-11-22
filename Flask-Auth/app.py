from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from flask_migrate import Migrate
from models import db
from models import LoginForm, RegisterForm



app = Flask(__name__)


migrate = Migrate(app, db)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'thisisasecretkey'

db.init_app(app)

@app.route('/')
def home ():
    return render_template('home.html')

@app.route('/login', methods = ['GET', 'POST'])
def login ():

    form = LoginForm()

    return render_template('login.html', form = form)

@app.route('/register', methods = ['GET', 'POST'])
def register():

    form = RegisterForm()

    return render_template('register.html', form = form)

if __name__ == '__main__':
    app.run(debug=True)