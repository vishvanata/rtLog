DELIMITER $$
USE rtumv

DROP procedure IF EXISTS spCheckSlno;

CREATE PROCEDURE spCheckSlno(
IN p_slno varchar(50)
)
BEGIN
SELECT 
       slno, inactive
FROM umv
WHERE  slno = p_slno;

END
$$
