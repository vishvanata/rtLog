drop table umvUsers;
CREATE TABLE if not exists umvUsers(
        slno VARCHAR(50) NOT NULL,
	email VARCHAR(60) NOT NULL,
        fname VARCHAR(60),
        lname VARCHAR(60),
        PRIMARY KEY (slno,email)
);
