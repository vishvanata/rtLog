from config import SQLConfig
from sqlalchemy import create_engine
from decimal import *
import pysal
from pysal.cg.kdtree import KDTree
from flask import Flask, json, Response
from flask_jsonpify import jsonify

# create database engine (SQLAlchemy db pool)
sql_string = 'mysql://' + SQLConfig.USER_ID + ':' + SQLConfig.PASSWORD + '@' + SQLConfig.IP + '/' + SQLConfig.DB
engine = create_engine(sql_string)

def LL():
  mysql_stmt = 'select mac,description,current_latitude,current_longitude from umv'
  result = engine.execute(mysql_stmt)
  myLocations = []
  myData = []

  for row in result:
    myLocations.append((float(row['current_latitude']), float(row['current_longitude'])))
    myData.append((row['description'],float(row['current_latitude']), float(row['current_longitude'])))

  tree = KDTree(myLocations, distance_metric='Arc', radius=pysal.cg.RADIUS_EARTH_MILES)
  current_point = (34.075375, -84.29409)
  # get all points within 29410 mile of 'current_point'
  indices = tree.query_ball_point(current_point, 500)
  response_dataset = []
  for i in indices:
    dict = {
    'description': myData[i][0],
    'current_latitude': myData[i][1],
    'current_longitude': myData[i][2]
    }
    response_dataset.append(dict)

  #return jsonify(data=response_dataset);
  return json.dumps(response_dataset);

response = LL();
print response
