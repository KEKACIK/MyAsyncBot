CREATE TABLE IF NOT EXISTS users(
    id          SERIAL              PRIMARY KEY,
    user_id     BIGINT  NOT NULL,
    login       TEXT,
    city        TEXT
);

CREATE TABLE days(
    day_id  SERIAL  NOT NULL    PRIMARY KEY,
    user_id BIGINT  NOT NULL,
    name    TEXT,
    dirty   REAL    NOT NULL    DEFAULT 1000
);

CREATE TABLE IF NOT EXISTS orders(
    order_id    SERIAL  NOT NULL    PRIMARY KEY,
    day_id      BIGINT NOT NULL,
    user_id     BIGINT  NOT NULL,
    address     TEXT,
    price       REAL NOT NULL
);

ALTER TABLE users owner TO postgres;
CREATE UNIQUE index users_id_uindex ON users (id);