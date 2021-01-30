# Vishva Natarajan

#List all unmanned vehicle
#returns status code 100 for NO Records Found.

from flask import Flask, json, Response
from flask_jsonpify import jsonify
from flask_restful import Resource,reqparse
from sqlalchemy import create_engine

class adminList(Resource):
      def __init__(self,**kwargs):
        self.db = kwargs['db'];
        self.conn = self.db.raw_connection();

      def get(self):
        try:
           # select all records
            cursor = self.conn.cursor();
            cursor.callproc('spAdminList');
            resultSet = cursor.fetchall();
            self.conn.close();

            # parse data which contains multiple rows into the umv records
            umvList = [];
            for umv in resultSet:
               umvDict = {
	         'slno': umv[0],
	         'email': umv[1],
	         'ipaddress': umv[2],
	         'description': umv[3],
	         'inactive': umv[4],
	         'home_latitude': umv[5],
	         'home_longitude': umv[6],
	         'current_latitude': umv[7],
	         'current_longitude': umv[8],
	         'createdatetime': umv[9],
	         'lastupdatetime': umv[10]
               };
               umvList.append(umvDict);
            return jsonify(data=umvList);

        except Exception as e:
            return {'error': str(e)}
