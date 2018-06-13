import os
from flask import (Flask, reader_template, jsonify, request, redirect)

app = Flask(__name__)

from flask_alchemy import SQLAlchemy
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI', '') or 'sqlite:///DataSets/belly_button_biodiversity.sqlite'

db = SQLAlchemy(app)

from .models import metadata

@app.before_first_request
def setup():
    db.drop_all()
    db.create_all()

@app.route('/')
def home():
    return render_template ('index.html')

@app.name('/names')
def names():
    return jsonify(names)

@app.route('/otu')
def otu():
    return jsonify(otu)

@app.route('/metadata/<sample>')
def metadata():
    return jsonify(metadata)

@app.route('/wfeq/<sample>')
def wfreq():
    return jsonify(wfreq)

@app.route('/samples/<sample>')
def sample():
    return jsonify(sample)


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

if __name__ = "__main__":
    app.run()
