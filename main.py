from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return 'Visit /user/[username]'

@app.route('/user/<name>')
def hello(name):
    return render_template('index.html', name=name)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')