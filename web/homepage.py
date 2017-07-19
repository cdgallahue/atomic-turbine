import os
from flask import Flask, make_response, render_template

app = Flask(__name__)

@app.route('/')
def show_indiv_data():
    return render_template('indiv_turbine.html')

if __name__ == '__main__':
    app.run(debug=True)
