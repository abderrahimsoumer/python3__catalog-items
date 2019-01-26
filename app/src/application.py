from models import Base, User, Category, Item, secret_key
from flask import render_template, Flask, flash, request, url_for, jsonify
from flask import abort, redirect
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.pool import StaticPool
from sqlalchemy import create_engine

# from flask_httpauth import HTTPBasicAuth
# auth = HTTPBasicAuth()
from flask import session as login_session
from pickle import dump
import json


engine = create_engine(
    'sqlite:///catalogItems.db',
    connect_args={'check_same_thread': False},
    poolclass=StaticPool, echo=True
    )

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()
app = Flask(__name__)


@app.route('/login/', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = session.query(User).filter_by(username=username).first()
        if not user or not user.verify_password(password):
            message = "Username and/or password incorrect"
            print(message)
            flash(message)
            return redirect(url_for('login'))
        login_session['id'] = user.id
        login_session['name'] = user.name
        login_session['username'] = user.username
        return redirect(url_for('index'))
    if request.method == "GET":
        if "username" in login_session:
            return redirect(url_for('index'))
        return render_template('login.html')


@app.route('/')
def index():
    categories = session.query(Category).all()
    # return jsonify(Category=[i.serialize for i in categories])
    return render_template('index.html', categories=categories)


@app.route('/users/', methods=['POST'])
def newUser():
    name = request.form.get('name')
    username = request.form.get('username')
    password = request.form.get('password')
    if username is None or password is None:
        print("missing arguments")
        abort(400)
    if session.query(User).filter_by(username=username).first() is None:
        user = User(username=username, name=name)
        user.hash_password(password)
        session.add(user)
        session.commit()
        print("save")
        return redirect(url_for('index'))

    else:
        message = "Usernam already taken"
        flash(message)
        print("Usernam already taken")
        return redirect(url_for('login'))


if __name__ == '__main__':
    app.secret_key = secret_key
    app.debug = True
    app.config['SECRET_KEY'] = secret_key
    app.run(host='0.0.0.0', port=5000)
