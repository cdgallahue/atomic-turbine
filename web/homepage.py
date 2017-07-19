import os
from datetime import datetime
from flask import Flask, make_response, render_template

app = Flask(__name__)

@app.route('/')
def show_indiv_data():
	timestamp = str(datetime.now())
    	return render_template('indiv_turbine.html', timestamp=timestamp)

if __name__ == '__main__':
    app.run(debug=True)
