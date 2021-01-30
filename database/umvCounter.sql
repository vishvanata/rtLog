drop table if exists umvCounter;
CREATE TABLE if not exists umvCounter(
        slno VARCHAR(50),
	email VARCHAR(60),
        count INTEGER,
	createdatetime TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (slno) REFERENCES  umvUsers(slno)
);
