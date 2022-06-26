-- CREATE SCHEMA stage;

CREATE TABLE stage.st_trips(
    st_region           VARCHAR(300),
    origin_coord        VARCHAR(300),
    destination_coor    VARCHAR(300),
    st_datetime         TIMESTAMP,
    st_datasource       VARCHAR(300),
    prttn_dt            TIMESTAMP
)

-- GRANT INSERT, SELECT, UPDATE, DELETE ON stage.st_trips TO aws_dev_red;
-- GRANT USAGE ON SCHEMA stage to aws_dev_red;