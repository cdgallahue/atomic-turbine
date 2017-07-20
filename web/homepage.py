import os
from datetime import datetime
from flask import Flask, make_response, render_template
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)

@app.route('/')
@cross_origin(origin='localhost',headers=['Content-Type','Authorization'])
def show_indiv_data():
	timestamp = str(datetime.now())
        return render_template('indiv_turbine.html', timestamp=timestamp)

def add_headers(response):
    """
    Fix for font-awesome files: after Flask static send_file() does its
    thing, but before the response is sent, add an
    Access-Control-Allow-Origin: *
    HTTP header to the response (otherwise browsers complain).
    """

    if (request.path):
        response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route('/download')
@cross_origin(origin='localhost',headers=['Content-Type','Authorization'])
def download():
	return "Downloading"
	
if __name__ == '__main__':
    app.run(debug=True)
