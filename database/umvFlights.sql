drop table umvFlights;
CREATE TABLE umvFlights(
        id MEDIUMINT NOT NULL AUTO_INCREMENT,
	slno VARCHAR(45) NOT NULL,
        email VARCHAR(60),
	ipaddress VARCHAR(15),
	description VARCHAR(200),
	home_latitude DECIMAL(10, 8) NOT NULL,
	home_longitude DECIMAL(11, 8) NOT NULL,
	current_latitude DECIMAL(10, 8) NOT NULL,
	current_longitude DECIMAL(11, 8) NOT NULL,
	createdatetime TIMESTAMP,
	enddatetime TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        PRIMARY KEY (id)
);

ALTER TABLE umvFlights
ADD UNIQUE INDEX ix_umvFlights (slno,ipaddress, createdatetime, current_latitude, current_longitude, home_latitude, home_longitude); 
