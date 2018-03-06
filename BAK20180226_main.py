from flask import Flask, render_template
from flask_mysqldb import MySQL
import MySQLdb, sys

app = Flask(__name__)
mysql = MySQL(app)
@app.route("/")

def index():
    db = MySQLdb.connect(host = "10.0.0.160", user = "temp", passwd = "letmein", db = "temp" )
    cursor = db.cursor()
    value = "SELECT Time, S1temp, S1humidity, S2temp, S2humidity, OWMtemp, OWMhumidity, OWMstatus FROM DHT22 ORDER BY Time DESC LIMIT 50"
    try:
        cursor.execute(value)
        print("reading OK")
    except MySQLdb.Error as e:
        print("Error %d: %s" % (e.args[0],e.args[1]))
    data = cursor.fetchall()
    cursor.close()
    db.close()
    return render_template("index.html", data=data)


@app.route("/history/<tables>")
def history(tables):
    return render_template("history.html", tables=tables)



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")


