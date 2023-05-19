import os
from dotenv import load_dotenv
basedir = os.path.abspath(os.path.dirname(__file__))
#access to the project in ANY OS
#allow outside file/folders added

load_dotenv(os.path.join(basedir, '.env'))

class Config():
    """
    Set config variables for the flask app
    using environment var where avail
    otherwise cretae the the config var if not done
    already
    """

    FLASK_APP = os.environ.get('FLASK_APP')
    FLASK_ENV = os.environ.get('FLASK_ENV')
    SECRET_KEY = os.environ.get("SECRET_KEY") or "idk"
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or "sqlite:///" + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False 
