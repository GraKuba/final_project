from classes import DataFrame
from flask import Flask, render_template, request

app = Flask(__name__)

dt = DataFrame


@app.route('/', methods=['GET', 'POST'])
def index():
    data = request.form
    city = data.getlist('city')
    dt(city)
    return render_template('index.html')


