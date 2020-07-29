from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello world'

@app.route('/RiversideRocks')
def cakes():
    return 'Look its Riverside Rocks!'

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')