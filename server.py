from flask import Flask, render_template
from get_map import create_map
from test import test

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/getMap")
def getMap():
    testResult = test()
    create_map(testResult, '80301')
    return render_template('map.html')

if __name__ == "__main__":
    app.run(debug=True)
