curl -i -H "Content-Type: application/json" -X POST -d '
{
   "slno": "GATES-00:22:494A",
   "email": "zx@rtlogserver.org",
   "ipaddress": "192.168.0.180",
   "description" :  "Flight History tests-2",
   "latitude": 75.400702,
   "longitude": -71.065744,
   "inactive" : 1
}' http://localhost:5000/rtLog/v1.0/log
