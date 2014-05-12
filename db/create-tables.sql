CREATE TABLE msw_user (
	id INTEGER,
	username VARCHAR(20),
	firstname VARCHAR(20),
	lastname VARCHAR(20),
	password VARCHAR(20),
	accountnumber VARCHAR(20),
	phone VARCHAR(20),
	address VARCHAR(200),
	email VARCHAR(200)
);

CREATE TABLE msw_tran_stock (
	id INTEGER,
	descriptoin VARCHAR(200),
	accountnumber VARCHAR(20),
	amount INTEGER,
	tickersymbol VARCHAR(20),
	trantype ENUM('sell', 'buy'),
	trantime DATETIME
);

CREATE TABLE msw_tran_tranfer (
	id INTEGER,
	descriptoin VARCHAR(200),
	accountnumber VARCHAR(20),
	exaccountnumber VARCHAR(20),
	amount INTEGER,
	trantime DATETIME
);

CREATE TABLE msw_account(
	accountnumber VARCHAR(20),
	balance INTEGER
);

CREATE TABLE msw_stock(
	tickersymbol VARCHAR(20),
	accountnumber VARCHAR(20),
	shares INTEGER
);

CREATE TABLE msw_external_account(
	accountnumber VARCHAR(20),
	exaccountnumber VARCHAR(20),
	exswiftcode VARCHAR(20)
);