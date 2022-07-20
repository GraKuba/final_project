from classes import DataFrame
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    data = request.form
    city = data.get('city')
    dt = DataFrame(city)
    # AVERAGES
    positions_and_averages = dt.average_income()
    # HIGHEST PAYING COMPANIES
    highest_paying = dt.highest_paying_companies()
    # SALARY IN COMPARISON
    salary_comparison = dt.salary_in_comparison()
    # MOST PROFITABLE POSITION AT A COMPANY
    most_profitable = dt.most_profitable_position()
    statements = ['Average pay per position:', 'Top 3 highest paying companies:',
                  'Top 3 companies salary in comparison with the average:', 'Most profitable positions:']
    if city:
        city = city + " - "
        statements = statements

    else:
        city = ""
        statements = ""

    return render_template('index.html', statements=statements, city=city,
                           positions_and_averages=positions_and_averages, highest_paying=[highest_paying],
                           salary_comparison=salary_comparison, most_profitable=most_profitable)
