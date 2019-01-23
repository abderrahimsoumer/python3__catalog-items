from models import Base, User, Category, Item
from flask import render_template, Flask, jsonify, request, url_for, abort,redirect, g
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy import create_engine

from flask_httpauth import HTTPBasicAuth
auth = HTTPBasicAuth()


engine = create_engine('sqlite:///catalogItems.db')

Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()
app = Flask(__name__)


#ADD @auth.verify_password decorator here
@auth.verify_password
def verify_password(username_or_token,password):
    #Try to see if it's a token first
    user_id = User.verify_auth_token(username_or_token)
    if user_id:
        user = session.query(User).filter_by(id= user_id).one()
    else:
        user = session.query(User).filter_by(username= username_or_token).first()
        if not user or not user.verify_password(password):
            return False
    g.user = user
    return True

    
@app.route('/login/')
def login():
	return render_template('login.html')

@app.route('/users/',methods=['POST'])
def newUser():
    name = request.form.get('name')
    username = request.form.get('username')
    password = request.form.get('password')
    if username is None or password is None:
        print("missing arguments")
        abort(400) 
    if session.query(User).filter_by(username= username).first() is None:
        user = User(username= username,name= name)
        user.hash_password(password)
        session.add(user)
        session.commit()
        print("save")
        return redirect(url_for('index'))

    else:
        message ="Usernam already taken"
        print("Usernam already taken")
        return redirect(url_for('login'))



@app.route('/')
@auth.login_required
def index():
	print("Index page")
	return "Index page"


if __name__ == '__main__':
    app.debug = True
    #app.config['SECRET_KEY'] = ''.join(random.choice(string.ascii_uppercase + string.digits) for x in xrange(32))
    app.run(host='0.0.0.0', port=5000)
