from flask import (Flask, render_template, abort, jsonify,
                    request, redirect, url_for)
from keys import create_key, key_exist, load_key
import pandas as pd
import plotly.graph_objects as go
import plotly
import json, csv
from model import get_stocks_data, create_candlestick_chart

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        symbol = request.form['stock_symbol']
        return redirect(url_for('stock_view', symbol=symbol))
    else:
        if key_exist():
            _key_exist = "True"
        return render_template("index.html", key_exist=_key_exist)

@app.route("/about/")
def about():
    return render_template("about.html")

@app.route("/stock/", methods=["GET", "POST"])
def stock():
    if request.method == "POST":
        symbol = request.form['stock_symbol']
        return redirect(url_for('stock_view', symbol=symbol))
    else:
        if key_exist():
            _key_exist = "True"
        return render_template("stock.html",key_exist=_key_exist)

@app.route("/stock/<string:symbol>", methods=["GET", "POST"])
def stock_view(symbol):
    if request.method == "POST":
        symbol = request.form['stock_symbol']
        return redirect(url_for('stock_view', symbol=symbol))
    try:
        stock_data, stock_overview = get_stocks_data(symbol.upper())
        intrinsic_value = float(stock_overview["EPS"]) * float(stock_overview["PERatio"])
        fig = create_candlestick_chart(stock_data, "Daily Time Series")
        graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)
        return render_template("stock_view.html", symbol=symbol, stock_data=stock_data, stock_overview=stock_overview, intrinsic_value=intrinsic_value, graphJSON=graphJSON)
    except IndexError:
        abort(404)
    except KeyError:
        if len(stock_overview) == 0:
            invalid_symbol = "True"
        else:
            invalid_symbol = "False"
        return render_template("error.html",invalid_symbol=invalid_symbol)


@app.route("/api_key/", methods=["GET", "POST"])
def api_key():
    if request.method == "POST":
        key = request.form['key']
        create_key(key)
        return redirect(url_for('stock'))
    else:
        if key_exist():
            _key_exist = "True"
        return render_template("key.html", key_exist=_key_exist)