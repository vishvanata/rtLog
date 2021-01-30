# Vishva Natarajan

#List all unmanned vehicle
#returns status code 100 for NO Records Found.

from flask import Flask, json, Response
from flask_jsonpify import jsonify
from flask_restful import Resource,reqparse
from sqlalchemy import create_engine

class List(Resource):
      def __init__(self,**kwargs):
        self.db = kwargs['db'];
        self.conn = self.db.raw_connection();

      def get(self):
        try:
           # select all records
            cursor = self.conn.cursor();
            cursor.callproc('spListAll');
            resultSet = cursor.fetchall();lllllllllllllllll
            self.conn.close();

            # parse data which contains multiple rows into the umv records
            umvList = [];
            for umv in resultSet:
               umvDict = {
	         'description': umv[0],
	         'current_latitude': umv[1],
	         'current_longitude': umv[2],
	         'createdatetime': umv[3],
	         'lastupdatetime': umv[4]
               };
               umvList.append(umvDict);
            return jsonify(data=umvList);

        except Exception as e:
            return {'error': str(e)}
