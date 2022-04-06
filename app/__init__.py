# initializes the application 
# creating a Flask app instance

from pathlib import Path
from flask import Flask

app = Flask(__name__)

app.config.from_object(Path('app', 'config'))

from app import routes