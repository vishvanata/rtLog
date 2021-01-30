# Vishva Natarajan

#List all unmanned vehicle
#returns status code 100 for NO Records Found.

from flask import Flask, json, Response
from flask_jsonpify import jsonify
from flask_restful import Resource,reqparse
from sqlalchemy import create_engine

class adminListFlights(Resource):
      def __init__(self,**kwargs):
        self.db = kwargs['db'];
        self.conn = self.db.raw_connection();

      def get(self):
        try:
           # select all records
            cursor = self.conn.cursor();
            cursor.callproc('spListFlights');
            resultSet = cursor.fetchall();
            cursor.close();
            self.conn.close();

            # parse data which contains multiple rows into the umv records
            umvList = [];
            for umv in resultSet:
               umvDict = {
	         'id': umv[0],
	         'slno': umv[1],
	         'email': umv[2],
	         'ipaddress': umv[3],
	         'home_latitude': umv[4],
	         'home_longitude': umv[5],
	         'current_latitude': umv[6],
	         'current_longitude': umv[7],
	         'description': umv[8],
	         'createdatetime': umv[9],
	         'enddatetime': umv[10]
               };
               umvList.append(umvDict);
            return jsonify(data=umvList);

        except Exception as e:
            return {'error': str(e)}
