DELIMITER $$
USE rtumv

DROP procedure IF EXISTS spListAll;

CREATE PROCEDURE spListAll()
BEGIN
SELECT 
	description,
	current_latitude,
	current_longitude,
	createdatetime,
	lastupdatetime
FROM umv
WHERE inactive = 0
ORDER BY createdatetime desc;

END
$$
