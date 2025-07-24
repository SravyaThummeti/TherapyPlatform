# backend/app/config.py
import os
from dotenv import load_dotenv

# this loads the .env file automatically
load_dotenv()

class Config:
    DEBUG = True
    SECRET_KEY            = os.environ['SECRET_KEY']
    JWT_SECRET_KEY        = os.environ['JWT_SECRET_KEY']
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    SQLALCHEMY_TRACK_MODIFICATIONS = False
