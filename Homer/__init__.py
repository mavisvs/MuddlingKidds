import os
from flask import Flask, session, request
#from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request
zipcode = ""
app = Flask(__name__)

import Homer.views

@app.route('/results', methods=["GET"])
def getZip():
    global zipcode
    zipcode = request.args.get('zip')
    return zipcode