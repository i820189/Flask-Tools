from flask import Flask

app = Flask(__name__)

if app.config["ENV"] == "Production":
  app.config.from_object("config.ProductionConfig")
  
elif app.config["ENV"] == "Testing":
  app.config.from_object("config.TestingConfig")
else:
  app.config.from_object("config.DevelopmentConfig")

from app import views
from app import admin_views