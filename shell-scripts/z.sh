
curl -i -H "Content-Type: application/json" -X POST -d '
{
   "mac": "4A-0A-B3-E5-49-44",
   "ipaddress": "192.168.0.180",
   "description" :  "DJI Phantom 4 Quadcopter",
   "latitude": 33.9412127,
   "longitude": -84.21353090000002,
   "inactive" : 0
}' http://vishva.mynetgear.com:70/rtLog/v1.0/log
