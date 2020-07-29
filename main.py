from flask import Flask, render_template, request
from flaskext.mysql import MySQL
import pymysql
import json


db = pymysql.connect("localhost", "root", "", "python")


app = Flask(__name__)


@app.route('/')
def index():
    return 'Visit /user/[username]'

@app.route('/user/<name>')
def hello(name):
    name = name
    cursor = db.cursor()
    sql = "SELECT * FROM users WHERE Username='Tucker'"
    cursor.execute(sql)
    results = cursor.fetchall()
    sql = json.loads(str(results))
    user = sql[1]
    return render_template('index.html', user=user, name=name)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')