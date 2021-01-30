DELIMITER $$
USE rtumv

DROP procedure IF EXISTS spListFlights;

CREATE PROCEDURE spListFlights()
BEGIN
SELECT 
        id,
        slno,
        email,
        ipaddress,
	home_latitude,
	home_longitude,
	current_latitude,
	current_longitude,
	description,
	createdatetime,
	enddatetime
FROM umvFlights
ORDER BY enddatetime desc;

END
$$
