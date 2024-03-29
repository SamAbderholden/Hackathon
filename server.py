from flask import Flask, render_template, request
from get_map import create_map
import bcbs
import kaiser
import medicare
import aetna
import cigna 

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
        bcbsdata = bcbs.get_data(plan, zipcode)
        bcbsstatus = create_map(bcbsdata, zipcode)
        if(bcbsstatus != 0):
            return render_template('map.html')
        return render_template('error.html')
    if(provider == 'Kaiser Permanente'):
        kaiserdata = kaiser.get_data(zipcode, plan)
        kaiserstatus = create_map(kaiserdata, zipcode)
        if(kaiserstatus != 0):
            return render_template('map.html')
        return render_template('error.html')
    if(provider == 'Medicare'):
        medicaredata = medicare.get_data(zipcode)
        medicarestatus = create_map(medicaredata, zipcode)
        if(medicarestatus != 0):
            return render_template('map.html')
        return render_template('error.html')
    if(provider == 'Aetna'):
        aetnadata = aetna.get_data(zipcode, plan)
        aetnastatus = create_map(aetnadata, zipcode)
        if(aetnastatus != 0):
            return render_template('map.html')
        return render_template('error.html')
    if(provider == 'Cigna'):
        cignadata = cigna.get_data(zipcode, plan)
        cignastatus = create_map(cignadata, zipcode)
        if(cignastatus != 0):
            return render_template('map.html')
        return render_template('error.html')
    if(provider == 'Medicaid'):
        #TODO
        pass
    if(provider == 'United Healthcare'):
        #TODO
        pass
    if provider == 'Humana':
        #TODO
        pass
    return render_template('index.html')

    


if __name__ == "__main__":
    app.run(debug=True)
