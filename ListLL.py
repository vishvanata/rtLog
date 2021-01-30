# Vishva Natarajan

#List all unmanned vehicle
#returns status code 100 for NO Records Found.

from flask import Flask, json, Response
from flask_jsonpify import jsonify
from flask_restful import Resource,reqparse
from sqlalchemy import create_engine
import pysal
from pysal.cg.kdtree import KDTree

class ListLL(Resource):
      def __init__(self,**kwargs):
        self.db = kwargs['db'];
        self.conn = self.db.raw_connection();

      def get(self):
        try:
            # Parse the arguments
            parser = reqparse.RequestParser();
            parser.add_argument('latitude', type=float);
            parser.add_argument('longitude', type=float);
            args = parser.parse_args();

            _input_lat = args['latitude']
            _input_long = args['longitude']

            print "input lat and long : "
            print _input_lat
            print _input_long

            # select all records
            cursor = self.conn.cursor();
            cursor.callproc('spListLL');
            resultSet = cursor.fetchall();
            cursor.close();
            self.conn.close();

            # parse data which contains multiple rows into the umv records
            umvList = [];
            myLocations = []
            myData = []
            for umv in resultSet:
                lat = float(umv[1])
                long = float(umv[2])
                myLocations.append((lat, long))
                myData.append((str(umv[0]), lat, long, umv[3], umv[4]))


            tree = KDTree(myLocations, distance_metric='Arc', radius=pysal.cg.RADIUS_EARTH_MILES)
            print "inside  the process logic..."
            current_point = (_input_lat, _input_long)
            # get all points within 1 mile of 'current_point'
            indices = tree.query_ball_point(current_point, 500)
            final_results = [];

            for i in indices:
                myjsonData = {
                    'description': myData[i][0],
                    'current_latitude': myData[i][1],
                    'current_longitude': myData[i][2],
                    'lastupdatetime': myData[i][3],
                    'createdatetime': myData[i][4],
                };
                final_results.append(myjsonData);
            return jsonify(data=final_results);

        except Exception as e:
            return {'error': str(e)}
