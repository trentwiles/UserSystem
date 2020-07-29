from flask import Flask, render_template, request
from flaskext.mysql import MySQL
import pymysql

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
    return render_template('index.html', results=results, name=name)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')