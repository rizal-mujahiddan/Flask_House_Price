from flask import (
    Flask,
    render_template,
    request,
    jsonify
)

from Services.predict_price import predict_ml

import pandas as pd



app = Flask(__name__,template_folder='Views/')

@app.route("/",methods=['GET'])
def hello_world():
    return render_template('index.html')

@app.route("/form",methods=['POST'])
def process_form():
    form_data = request.form.to_dict()
    hasilnya = predict_ml(form_data)[0]
    return f"harganya adalah Rp{int(hasilnya)}"