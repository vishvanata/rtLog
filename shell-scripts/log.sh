echo "starting flight"
curl -i -H "Content-Type: application/json" -X POST -d '
{
   "slno": "GATES-00:22:494A",
   "email": "zx@natarajan.net",
   "ipaddress": "192.168.0.180",
   "description" :  "Flight History tests-2",
   "latitude": 75.400702,
   "longitude": -71.065744,
   "inactive" : 0
}' http://vishva.mynetgear.com:70/rtLog/v1.0/log

sleep 15;
echo "udating coordinates"
curl -i -H "Content-Type: application/json" -X POST -d '
{
   "slno": "GATES-00:22:494A",
   "email": "zx@natarajan.net",
   "ipaddress": "192.168.0.180",
   "description" :  "Flight History tests-2",
   "latitude": 77.400702,
   "longitude": -81.065744,
   "inactive" : 0
}' http://vishva.mynetgear.com:70/rtLog/v1.0/log

sleep 15;
echo "udating coordinates"
curl -i -H "Content-Type: application/json" -X POST -d '
{
   "slno": "GATES-00:22:494A",
   "email": "zx@natarajan.net",
   "ipaddress": "192.168.0.180",
   "description" :  "Flight History tests-2",
   "latitude": 67.400702,
   "longitude": -61.065744,
   "inactive" : 0
}' http://vishva.mynetgear.com:70/rtLog/v1.0/log



sleep 15;
echo "udating coordinates and ending flight"
curl -i -H "Content-Type: application/json" -X POST -d '
{
   "slno": "GATES-00:22:494A",
   "email": "zx@natarajan.net",
   "ipaddress": "192.168.0.180",
   "description" :  "Flight History tests-2",
   "latitude": 97.400702,
   "longitude": -91.065744,
   "inactive" : 1
}' http://vishva.mynetgear.com:70/rtLog/v1.0/log

echo  "fight test done"


#echo "select slno,description,home_latitude,home_longitude,current_latitude,current_longitude from umv where slno = 'GATES-00:22:494A'" | mysql -u pi -p rtumv
