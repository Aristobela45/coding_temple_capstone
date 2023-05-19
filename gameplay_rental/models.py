from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import uuid
from datetime import datetime

#security for passwords
from werkzeug.security import generate_password_hash, check_password_hash

#generate token for each user
import secrets 

from flask_login import UserMixin, LoginManager

from flask_marshmallow import Marshmallow
db = SQLAlchemy()
login_manager = LoginManager()
ma = Marshmallow()

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)


class User(db.Model, UserMixin):
    id = db.Column(db.String, primary_key = True)
    first_name = db.Column(db.String(150), nullable = True, default = '')
    last_name = db.Column(db.String(150), nullable = True, default = '')
    email = db.Column(db.String(150), nullable = False)
    password = db.Column(db.String(150), nullable = True, default = '')
    username = db.Column(db.String(150), nullable = False)
    token = db.Column(db.String, default = '', unique = True)
    date_created = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)


    def __init__(self, email, username, first_name = '', last_name = '', id = '', password = ''):
        self.id = self.set_id()
        self.first_name = first_name
        self.last_name = last_name
        self.password = self.set_password(password)
        self.email = email
        self.username = username
        self.token = self.set_token(24)

    def set_token(self, length):
        return secrets.token_hex(length)
    
    def set_id(self):
        return str(uuid.uuid4())
    
    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)
        return self.pw_hash
    
    def __repr__(self):
        return f"User {self.email} has been added to the database!"
    

class Game(db.Model):
    id = db.Column(db.String, primary_key = True)
    search = db.Column(db.String(200), nullable = True)
    search_precise = db.Column(db.Boolean)
    search_exact = db.Column(db.Boolean)
    platforms = db.Column(db.String(200), nullable = True)
    stores = db.Column(db.String(200), nullable = True)
    developers = db.Column(db.String(200), nullable = True)
    dates = db.Column(db.String(200), nullable = True)
    publishers = db.Column(db.String(200), nullable = True)
    user_token = db.Column(db.String, db.ForeignKey('user.token'), nullable = False)

    def __init__(self, search, search_precise, search_exact, platforms, stores, developers, dates, publishers, user_token):
        self.id = self.set_id()
        self.search = search
        self.search_precise = search_precise
        self.search_exact = search_exact
        self.platforms = platforms
        self.stores = stores
        self.developers = developers
        self.dates = dates
        self.publishers = publishers
        self.user_token = user_token
    #   game_search = request.json['search']
    def set_id(self):
        return str(uuid.uuid4())
    
    def __repr__(self):
        return F"Game {self.search_exact} have been added!"
    
class gameSchema(ma.Schema):
    class Meta:
        fields = ['id', 'search', 'search_precise', 'search_exact', 'platforms', 'stores', 'developers', 'dates', 'publishers']

game_schema = gameSchema()
games_schema = gameSchema(many = True)