DELIMITER $$
USE rtumv

DROP procedure IF EXISTS spUpdate;

CREATE PROCEDURE spUpdate (
IN p_slno varchar(50),
IN p_email varchar(60),
IN p_ipaddress varchar(15),
IN p_latitude DECIMAL(10, 8), 
IN p_longitude DECIMAL(11, 8),
IN p_inactive  tinyint(1)
)
BEGIN
   -- if existing record is reactivated (ie. the drone is taking a new flight
   -- this is reactivation and then the home lat and long is going to be the current lat and long.

	update umv set
    		ipaddress = p_ipaddress,
    		current_latitude = p_latitude,
    		current_longitude = p_longitude,
    		inactive = p_inactive,
    		lastupdatetime = CURRENT_TIMESTAMP
	where 
     		slno = p_slno AND
                email = p_email;
	
END
$$
