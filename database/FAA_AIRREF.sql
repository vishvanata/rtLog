drop table if exists FAA_AIRREF;
CREATE TABLE FAA_AIRREF(
	CODE VARCHAR(15),
	MFR VARCHAR(50),
	MODEL VARCHAR(45),
	TYPE_ACFT VARCHAR(50),
	TYPE_ENG VARCHAR(50),
	AC_CAT VARCHAR(20),
	BUILD_CERT_IND VARCHAR(20),
	NO_ENG VARCHAR(5),
	NO_SEATS VARCHAR(10),
	AC_WEIGHT VARCHAR(10),
	SPEED VARCHAR(10)
);
