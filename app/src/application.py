from models import Base, User, Category, Item, secret_key
from flask import render_template, Flask, flash, request, url_for, jsonify
from flask import abort, redirect
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.pool import StaticPool
from sqlalchemy import create_engine, exc

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
        login_session['user_id'] = user.id
        login_session['name'] = user.name
        login_session['username'] = user.username
        return redirect(url_for('index'))
    if request.method == "GET":
        if "username" in login_session:
            return redirect(url_for('index'))
        return render_template('login.html')


@app.route('/logout/')
def logout():
    login_session.pop('user_id',None)
    login_session.pop('username',None)
    login_session.pop('name',None)
    return redirect(url_for('index'))


@app.route('/')
def index():
    categories = session.query(Category).all()
    latest_items = session.query(Item).limit(20).all()
    """
    Instead of using this code to get the information for the user actif
    I just store the information I need in the session

    user_actif = None
    if "username" in login_session:
        user_actif = session.query(User).filter_by(
                     username= login_session.get('username')
                    ).first()
    """
    return render_template('index.html', categories=categories, items= latest_items)


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
        print(message)
        return redirect(url_for('login'))


@app.route('/new-item/', methods=['GET','POST'])
def newItem():
    # The user can only add an item if he logged in
    if "username" not in login_session:
            return redirect(url_for('login'))

    if request.method == 'POST':
        title = request.form.get('title')
        description = request.form.get('description')
        category_id = request.form.get('category')
        user_id = login_session.get('user_id')
        # title, description and category_id must not be empty
        if not title or not description or not category_id:
            message = "Please, Enter all the fields"
            flash(message)
            return redirect(url_for('newItem'))
        item = Item(title=title, description=description,
                    cat_id= category_id, user_id=user_id
                    )
        session.add(item)
        try:
            session.commit()
            message = "added successfully"
            flash(message)
        except exc.SQLAlchemyError as e:
            print(str(e))
            message = "Unable to save changes"
            flash(message)
        return redirect(url_for('newItem'))

    if request.method == 'GET':
        categories = session.query(Category).all()
        return render_template('ajoute.html',categories=categories)


@app.route('/item/<int:id>')
def itemView(id):
    try:
        item = session.query(Item).filter_by(id=id).first()
    except exc.SQLAlchemyError as e:
        abort(404)
    
    return render_template('detail.html',item=item)

@app.route('/item/edit/<int:id>')
def itemUpdate(id):
    return "Update"


@app.route('/item/delete/<int:id>')
def itemDelete(id):
    return "Delete"


if __name__ == '__main__':
    app.secret_key = secret_key
    app.debug = True
    app.config['SECRET_KEY'] = secret_key
    app.run(host='0.0.0.0', port=5000)
