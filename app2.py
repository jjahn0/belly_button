import os
import json
from flask import (Flask, render_template, jsonify, request, redirect)
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy import inspect
from sqlalchemy.sql import func
from pprint import pprint
from collections import Counter
import numpy as np
import plotly as plt

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI', '') or 'sqlite:///DataSets/belly_button_biodiversity.sqlite'

db = SQLAlchemy(app)

Base = automap_base()
engine = create_engine("sqlite:///DataSets/belly_button_biodiversity.sqlite")
Base.prepare(engine, reflect=True)
session = Session(engine)

# from .models import metadata

@app.before_first_request
def setup():
    db.drop_all()
    db.create_all()

@app.route('/')
def home():
    return render_template ('index.html')

# @app.name('/names')
# def names():
#     return jsonify(names)

@app.route('/otu')
def otu():
    Otu = Base.classes.otu
    otuID = session.query(Otu.otu_id).all()
    return jsonify(otuID)

@app.route('/metadata/<sample>')
def metadata():
    Samples_metadata = Base.classes.samples_metadata
    return jsonify(Samples_metadata)

# @app.route('/wfeq/<sample>')
# def wfreq():
#     return jsonify(wfreq)

@app.route('/samples/<sample>')
def sample():
    Samples = Base.classes.samples
    return jsonify(Samples)

@app.route('/api/metadata')
def metadb():
    # results = db.session.query(***)
    hover_text = ''
    values = ''
    labels = ''

    belly_data = [{
        'type': 'pie',
        'value': '',
        'label': '',
        'text': hover_text,
        'hoverinfo': 'text',
    }]
    return jsonify(belly_data)

if __name__ == "__main__":
    app.run()
