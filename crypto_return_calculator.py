from flask import Flask, render_template, request
from datetime import date
import datetime
import requests

app = Flask(__name__)


def format_date_str(_str):
    year = _str[0:4]
    day = _str[8:]
    month = _str[5:7]

    newstr = day + '-' + month + '-' + year

    return newstr


@app.route("/")
def index():
    return render_template("index.html", result="See how your cryptocurrency investments would have grown over time")


@app.route("/calculate", methods=["POST"])
def calculate():
    investment_amount = float(request.form.get("investment-amount"))
    cryptocurrency = request.form.get("cryptocurrency")
    investment_date = request.form.get("investment-date")
    investment_date = format_date_str(investment_date)

    print(investment_date, investment_amount, cryptocurrency)

    # get actual price
    url = f'https://api.coingecko.com/api/v3/simple/price?ids={cryptocurrency}&vs_currencies=usd'
    response = requests.get(url).json()

    actual_price = response[cryptocurrency]['usd']

    print(actual_price)

    # get old price
    url = f'https://api.coingecko.com/api/v3/coins/{cryptocurrency}/history?date={investment_date}&localization=false'
    response = requests.get(url).json()

    print(url)

    old_price = response['market_data']['current_price']['usd']

    # presenting result
    amount = investment_amount / old_price
    amount = amount * actual_price
    print(amount)
    amount = "{:,.2f}".format(amount)

    result_text = f'If I invested ${investment_amount} in {cryptocurrency} in {investment_date}, now I would have ${amount}!'

    return render_template('index.html', result=result_text)

if __name__ == "__main__":
    app.run(debug=True)


