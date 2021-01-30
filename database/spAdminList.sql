DELIMITER $$
DROP procedure IF EXISTS spAdminList;

CREATE PROCEDURE spAdminList()
BEGIN
SELECT 
	slno,
        email,
        ipaddress,
        description,
        inactive,
	home_latitude,
	home_longitude,
	current_latitude,
	current_longitude,
	createdatetime,
	lastupdatetime
FROM umv 
ORDER BY createdatetime desc;
END
$$
