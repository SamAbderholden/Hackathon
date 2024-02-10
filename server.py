from flask import Flask, render_template, request
from get_map import create_map
from bcbs import get_data

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/getMap")
def getMap():
    zipcode = request.args.get('zipcode')
    plan = request.args.get('plan')
    provider = request.args.get('provider')
    if(provider == 'Blue Cross Blue Shield'):
        testResult = get_data(plan, zipcode)
        create_map(testResult, zipcode)
    return render_template('map.html')

if __name__ == "__main__":
    app.run(debug=True)
