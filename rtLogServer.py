# Vishva Natarajan

# Main UMV (Un Manned Vehicles) RESTful API Server to start
# This imports the various API provided
#

import sys
sys.path.append("admin")

# import modules required
from flask import Flask,render_template
from flask_restful import Resource, Api, reqparse
from sqlalchemy import create_engine
from flask_cors import CORS, cross_origin
from json2html import *

# import modules written for this project
from log import log
from List import List
from ListLL import ListLL
from adminList import adminList
from adminListFlights import adminListFlights
from config import SQLConfig

# create database engine (SQLAlchemy db pool)
sql_string = 'mysql://' + SQLConfig.USER_ID + ':' + SQLConfig.PASSWORD + '@' + SQLConfig.IP + '/' + SQLConfig.DB;
print sql_string
db = create_engine(sql_string);

# Create instance of Flask class.
app = Flask(__name__)
app = Flask(__name__, static_url_path='')
CORS(app)

# Create instance of API from flask-restful
# flask-restful provides the modules that help us create easy APIs in Python and flask.

api = Api(app)

# Now, list the APIs provided, the route path, input arguments if any
# here,  we are passing the db object as an input argument.

api.add_resource(log, '/rtLog/v1.0/log', resource_class_kwargs={ 'db': db });
api.add_resource(List, '/rtLog/v1.0/list', resource_class_kwargs={ 'db': db });
api.add_resource(adminList, '/rtLog/v1.0/admin/list', resource_class_kwargs={ 'db': db });
api.add_resource(adminListFlights, '/rtLog/v1.0/admin/listFlights', resource_class_kwargs={ 'db': db });

#under development
api.add_resource(ListLL, '/rtLog/v1.0/listLL', resource_class_kwargs={ 'db': db });

# Display the RTlog website as the homepage
@app.route('/')
def root():
    return app.send_static_file('index.html')

# Start Server
if __name__ == '__main__':
    app.run(debug=True)
