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
    query = "SELECT * FROM people WHERE name='%s'"
    cursor.execute(query, [name])
    # https://github.com/RiversideRocks/UserSystem/issues/1
    user = cursor.fetchall()
    return render_template('index.html', user=user, name=name)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
