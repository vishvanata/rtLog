DELIMITER $$
USE rtumv

DROP procedure if exists spValidateUser;

CREATE PROCEDURE spValidateUser(
IN p_email varchar(60),
IN p_slno varchar(50),
OUT o_valid INT
)
BEGIN
  DECLARE v_email_exists INT;
  DECLARE v_flight_counter INT;
  
  SET v_email_exists = 0;
  SET v_flight_counter = 0;

  SELECT count(*) INTO v_email_exists FROM umvUsers 
  WHERE email = p_email AND slno = p_slno;

  IF (v_email_exists > 0) THEN
     SELECT count INTO v_flight_counter FROM umvCounter 
     WHERE email = p_email AND
           slno = p_slno  AND 
           `createdatetime` > NOW() - INTERVAL 1 HOUR;
  END IF;

  IF (v_flight_counter > 20) THEN
    SET o_valid = 0;
  ELSE
    SET o_valid = 1;
  END IF;
 
END
$$
