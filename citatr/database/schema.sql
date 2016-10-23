DROP TABLE if exists users;
CREATE TABLE users (
  id integer primary key autoincrement,
  username text NOT NULL UNIQUE,
  password text NOT NULL
);