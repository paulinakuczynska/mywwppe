# initializes the application 
# creating a Flask app instance

from flask import Flask
from config import Config

app = Flask(__name__)

app.config.from_object(Config)

from app import routes