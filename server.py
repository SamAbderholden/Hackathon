from flask import Flask, render_template
from get_map import create_map
from bcbs import get_data

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/getMap")
def getMap():
    testResult = get_data()
    create_map(testResult, '60048')
    return render_template('map.html')

if __name__ == "__main__":
    app.run(debug=True)
