BEGIN TRANSACTION;
CREATE TABLE users(id INTEGER PRIMARY KEY, username text, email text, phone text, website text, regdata text);
INSERT INTO "users" VALUES(1,'Kim','kim@naver.com','010-1234-1234','kim.com','2020-02-05 22:51:41');
INSERT INTO "users" VALUES(2,'goodsoul','park@daum.net','010-2222-3333','park.com','2020-02-05 22:51:41');
INSERT INTO "users" VALUES(3,'badboy','lee@naver.com','010-4444-5555','lee.com','2020-02-05 22:51:41');
INSERT INTO "users" VALUES(4,'Cho','cho@daum.net','010-5555-1234','cho.com','2020-02-05 22:51:41');
INSERT INTO "users" VALUES(5,'goodman','yoo@gmail.com','010-6666-1111','you.com','2020-02-05 22:51:41');
COMMIT;
