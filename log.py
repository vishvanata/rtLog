# Vishva Natarajan

#log an unmanned vehicle
#This class accepts 1 argument,the database connection
#This is an implementation for the RESTful service POST operation
#It parses the the input arguments received via the POST operation and stores
#the data into the database by calling a storedProc spRegister
#returns status code 200 for Success.
#returns status code 1000 for errors along with errorText

from flask import Flask
from flask_restful import Resource,reqparse
from sqlalchemy import create_engine

class log(Resource):
      def __init__(self,**kwargs):
        self.db = kwargs['db'];
        self.conn = self.db.raw_connection();

      def post(self):
        try:
            # Parse the arguments
            parser = reqparse.RequestParser();
            parser.add_argument('slno', type=str, help='slno address of device');
            parser.add_argument('email', type=str, help='slno address of device');
            parser.add_argument('ipaddress', type=str, help='ipaddres of device');
            parser.add_argument('description', type=str, help='ipaddres of device');
            parser.add_argument('latitude', type=str, help='current latititude');
            parser.add_argument('longitude', type=str, help='current longitude');
            parser.add_argument('inactive', type=str, help='true if landed');

            args = parser.parse_args();

            _slno = args['slno'];
            _email = args['email'];
            _ipaddress = args['ipaddress'];
            _description = args['description'];
            _latitude = args['latitude'];
            _longitude = args['longitude'];
            _inactive = args['inactive'];


            #if input is true/false or 0/1 passed,  ensure right value is set

            if(_inactive.lower() != 'true' and _inactive != '1'):
               _inactive = 0;
            else:
               _inactive = 1;

            # first validate the user
            #print "calling spValidateUser..."
            #rows_affected=0;
            #args = [_slno,_email,0,]
            #cursorX = self.conn.cursor();
            #cursorX.callproc('spValidateUser',args);
            #data = cursorX.fetchall();
            #print data
            #authFlag = data[1];
            #cursorX.close();
            #print "authFlag..."
            #print authFlag;
            #if authFlag == 0:
              #return {'StatusCode':'1000','Message': str('email and slno not valid! Register please!.')}

            print "calling spCheckSlno..."
            # first check drone status (if already exists or inactive)
            cursor = self.conn.cursor();
            rows_affected=0;
            cursor.callproc('spCheckSlno',(_slno,));
            data = cursor.fetchall();
            rows_affected=cursor.rowcount;
            cursor.close();

            # if umv already exists and inactive, just reactivate it.
            # else create it.

            if(rows_affected == 0): #new record
              cursor2 = self.conn.cursor();
              # insert row into database
              cursor2.callproc('spRegister',(_slno,_email,_ipaddress,_description,_latitude,_longitude));
              data = cursor2.fetchall();
              cursor2.close();

              if len(data) is 0:
               self.conn.commit();
               self.conn.close();
               return {'StatusCode':'200','Message': 'Registered Successfully'}
              else:
               self.conn.close();
               return {'StatusCode':'1000','Message': str(data[0])}
            else: #existing  record
              cursor2 = self.conn.cursor();
              cursor2.callproc('spUpdate',(_slno,_email,_ipaddress,_latitude,_longitude,_inactive));
              data = cursor2.fetchall();
              cursor2.close();

              #insert row in FlightsHistory
              outMessage="Message:  ";
              if _inactive == 1:
                 print("*** Creating record in umvFlights... ***");
                 cursor3 = self.conn.cursor();
                 cursor3.callproc('spUmvFlights',(_slno,_email,_ipaddress,_latitude,_longitude));
                 data = cursor3.fetchall();
                 cursor3.close();
                 outMessage = outMessage + "Flight history record created.";

              if len(data) is 0:
               self.conn.commit();
               self.conn.close();
               if _inactive ==1:
                 return {'StatusCode':'1000','Message': 'updated successfully and flight history rec created'}
               else:
                 return {'StatusCode':'1000','Message': 'updated successfully'}
              else:
               self.conn.close();
               return {'StatusCode':'1000','Message': str(data[0])}

        except Exception as e:
            return {'error': str(e)}
