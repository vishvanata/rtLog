from flask import Flask
from flask_restful import Resource,reqparse
from flask.ext.mysql import MySQL

class Register(Resource):
      def __init__(self,**kwargs):
        self.conn = kwargs['conn'];

      def post(self):
        try:
            # Parse the arguments
            parser = reqparse.RequestParser();
            parser.add_argument('mac', type=str, help='mac address of device');
            parser.add_argument('ipaddress', type=str, help='ipaddres of device');
            parser.add_argument('latitude', type=str, help='current latititude');
            parser.add_argument('longitude', type=str, help='current longitude');

            args = parser.parse_args();

            _mac = args['mac'];
            _ipaddress = args['ipaddress'];
            _latitude = args['latitude'];
            _longitude = args['longitude'];
            _description = "test";

           # insert row into database
            cursor = self.conn.cursor();
            cursor.callproc('spRegister',(_mac,_ipaddress,_description,_latitude,_longitude));
            data = cursor.fetchall();

            if len(data) is 0:
             self.conn.commit();
             return {'StatusCode':'200','Message': 'Registered Successfully'}
            else:
             return {'StatusCode':'1000','Message': str(data[0])}

        except Exception as e:
            return {'error': str(e)}
