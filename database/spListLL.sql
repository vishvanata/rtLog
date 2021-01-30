DELIMITER $$
USE rtumv

DROP procedure IF EXISTS spListLL;

CREATE PROCEDURE spListLL()
BEGIN
SELECT 
	description,
	current_latitude,
	current_longitude,
        lastupdatetime,
        createdatetime
FROM umv;

END
$$
