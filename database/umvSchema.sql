drop table umv;
CREATE TABLE umv(
	slno VARCHAR(45) NOT NULL,
        email VARCHAR(60),
	ipaddress VARCHAR(15),
	description VARCHAR(200) NULL,
	home_latitude DECIMAL(10, 8) NOT NULL,
	home_longitude DECIMAL(11, 8) NOT NULL,
	current_latitude DECIMAL(10, 8) NOT NULL,
	current_longitude DECIMAL(11, 8) NOT NULL,
	dest_latitude DECIMAL(10, 8),
	dest_longitude DECIMAL(11, 8),
	inactive BOOLEAN NOT NULL DEFAULT 0,
	admin_override BOOLEAN NOT NULL DEFAULT 0,
	admin_override_reason VARCHAR(200),
	admin_override_desc VARCHAR(200),
	createdatetime TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
	lastupdatetime TIMESTAMP NULL,
	enddatetime TIMESTAMP NULL,
	PRIMARY KEY (slno,email)
);
