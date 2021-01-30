DELIMITER $$
USE rtumv

DROP procedure IF EXISTS spRegister;

CREATE PROCEDURE spRegister (
IN p_slno varchar(50),
IN p_email varchar(60),
IN p_ipaddress varchar(15),
IN p_description varchar(200),
IN p_latitude DECIMAL(10, 8), 
IN p_longitude DECIMAL(11, 8)
)
BEGIN

insert into umv
(
    slno,
    email,
    ipaddress,
    description,
    home_latitude,
    home_longitude,
    current_latitude,
    current_longitude,
    inactive
)
values
(
    p_slno,
    p_email,
    p_ipaddress,
    p_description,
    p_latitude,
    p_longitude,
    p_latitude,
    p_longitude,
    FALSE
);

END
$$
