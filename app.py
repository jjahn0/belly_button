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

import pandas as pd

metadata_path = os.path.join('DataSets', 'Belly_Button_Biodiversity_Metadata.csv')
otu_id_path = os.path.join('DataSets', 'belly_button_biodiversity_otu_id.csv')
samples_path = os.path.join('DataSets', 'belly_button_biodiversity_samples.csv')
metadata_columns_path = os.path.join('DataSets', 'metadata_columns.csv')

metadataDF = pd.read_csv(metadata_path)
otuDF = pd.read_csv(otu_id_path)
samplesDF = pd.read_csv(samples_path)
metadataColDF = pd.read_csv(metadata_columns_path)

otu_samples = pd.merge(samplesDF, otuDF, on='otu_id', how='outer')
table = pd.pivot_table(otu_samples, columns=['otu_id'], aggfunc=np.sum)
otu_sample_DF = pd.DataFrame(table.sum()).rename(columns={0:'sample values'}).sort_values('sample values', ascending=False).reset_index().head(10)
pieData = pd.merge(otu_sample_DF, otuDF, on='otu_id', how='inner')

# @app.before_first_request
# def setup():
#     db.drop_all()
#     db.create_all()

@app.route('/')
def home():
    return render_template ('index.html')

# @app.name('/names')
# def names():
#     return jsonify(names)

# @app.route('/otu')
# def otu():
#     return jsonify(otu)

# @app.route('/metadata/<sample>')
# def metadata():
#     return jsonify(metadata)

# @app.route('/wfeq/<sample>')
# def wfreq():
#     return jsonify(wfreq)

# @app.route('/samples/<sample>')
# def sample():
#     return jsonify(sample)


@app.route('/api/samples')
def samples():
    hover_text = list(pieData['lowest_taxonomic_unit_found'])
    values = list(pieData['sample values'])
    labels = list(pieData['otu_id'])

    belly_data = [{
        'type': 'pie',
        'values': values,
        'labels': labels,
        'text': hover_text,
        'hoverinfo': 'text',
    }]
    return jsonify(belly_data)

if __name__ == "__main__":
    app.run(debug=True)
