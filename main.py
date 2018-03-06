from flask import Flask, render_template
from flask_mysqldb import MySQL
import MySQLdb, sys, fetcher

app = Flask(__name__)
mysql = MySQL(app)

@app.route("/")
def index():
    data = fetcher.temp_read()
    return render_template("index.html", data=data)

@app.route("/temps")
def temps():

    Out = fetcher.random_ints(48)
    Dator = fetcher.random_ints(48)
    Door = fetcher.random_ints(48)
    OverBed = fetcher.random_ints(48)
    UnderBed = fetcher.random_ints(48)

    #labels = fetcher.static_labels()
    #values = fetcher.RPi2()
    return render_template("temps.html", Out=Out, Dator=Dator, Door=Door, OverBed=OverBed, UnderBed=UnderBed)


@app.route("/simple_chart")
def chart():
    legend = "monthly data"
    labels = ["day 1", "day 2", "day 3", "day 4"]
    values = [10, 9, 8, 7, 6, 4, 7, 8]
    return render_template("chart.html", values=values, labels=labels)

@app.route("/temp")
def temp():
    legend = "monthly data"
    labels = fetcher.static_labels()
    values = fetcher.RPi2()
    return render_template("chart.html", values=values, labels=labels)

@app.route("/test")
def test():
    legend = "My test"
    labels = fetcher.static_labels()
    values = fetcher.RPi2()
    return render_template("chart_test.html", title="Bajskorv", max=35, values=values, labels=labels)

@app.route("/test/enkasse")
def enkasse():
    legend = 'Bajskorv'
    labels = fetcher.static_labels()
    values = fetcher.RPi2()
    return render_template("enkasse.html", values=values, labels=labels, legend = legend)

@app.route("/history/<tables>")
def history(tables):
    return render_template("history.html", tables=tables)



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")


