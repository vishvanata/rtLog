DELIMITER $$
USE rtumv

DROP procedure IF EXISTS spUmvFlights;

CREATE PROCEDURE spUmvFlights (
IN p_slno varchar(50),
IN p_email varchar(60),
IN p_ipaddress varchar(15),
IN p_latitude DECIMAL(10, 8), 
IN p_longitude DECIMAL(11, 8)
)
BEGIN

	DECLARE v_createdatetime TIMESTAMP;
	DECLARE v_home_latitude DECIMAL(10, 8);
	DECLARE v_home_longitude DECIMAL(11, 8);
	DECLARE v_description VARCHAR(200);

	select createdatetime,home_latitude,home_longitude,description
	into v_createdatetime,v_home_latitude,v_home_longitude,v_description
	from umv where slno = p_slno and email = p_email;

	insert into umvFlights
	(
    		slno,
                email,
    		ipaddress,
    		description,
    		home_latitude,
    		home_longitude,
    		current_latitude,
    		current_longitude,
    		createdatetime
	)
	values
	(
    		p_slno,
                p_email,
    		p_ipaddress,
    		v_description,
    		v_home_latitude,
    		v_home_longitude,
    		p_latitude,
    		p_longitude,
    		v_createdatetime
	);

        UPDATE umvCounter SET count = count + 1 WHERE email = p_email and slno = p_slno;

END
$$
