from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from sense_hat import SenseHat

app = Flask(__name__)
Bootstrap = Bootstrap(app)

#main route
@app.route("/")

def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='10.132.28.226')