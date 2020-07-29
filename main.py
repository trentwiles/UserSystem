from flask import Flask, render_template, request
from flaskext.mysql import MySQL
import pymysql

db = pymysql.connect("localhost", "root", "", "python")
api = Api(app)


app = Flask(__name__)


@app.route('/')
def index():
    return 'Visit /user/[username]'

@app.route('/user/<name>')
def hello(name):
    name=name
    cursor = db.cursor()
    sql = "SELECT * FROM table WHERE Username=name"
    cursor.execute(sql)
    results = cursor.fetchall()
    return render_template('index.html', results=results)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')