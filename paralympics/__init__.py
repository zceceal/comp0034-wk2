import os 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

def create_app(test_config=None):   
     # create the Flask app    
    app = Flask(__name__, instance_relative_config=True)    
    # configure the Flask app (see later notes on how to generate your o    
    app.config.from_mapping(
        SECRET_KEY='5scSELKpZoFu-HvGQ2nIMg',
        # Set the location of the database file called paralympics.sqlit   
        SQLALCHEMY_DATABASE_URI= "sqlite:///" + os.path.join(app.instanc))        
    
    with app.app_context():
        from paralympics import routes

    if test_config is None:        
    # load the instance config, if it exists, when not testing        
        app.config.from_pyfile('config.py', silent=True)    
    else:        
    # load the test config if passed in        
        app.config.from_mapping(test_config) 

    # ensure the instance folder exists    
    try:        
        os.makedirs(app.instance_path)

    except OSError:        
        pass    
    
    return app
