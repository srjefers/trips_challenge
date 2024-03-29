-- CREATE DATABASE analytics_db;
-- CREATE SCHEMA st_aux;

CREATE TABLE st_aux.st_trips_aux(
    st_region           VARCHAR(300),
    origin_coord_east   DOUBLE PRECISION,
    origin_coord_nort   DOUBLE PRECISION,
    destination_coord_east  DOUBLE PRECISION,
    destination_coord_nort  DOUBLE PRECISION,
    st_datetime         TIMESTAMP,
    st_datasource       VARCHAR(300)
)


-- COPY st_aux.st_trips_aux 
-- FROM 's3://anltcs-bckt-st/stage/st_trips/prttn_dt=20220626/' 
-- iam_role 'arn:aws:iam::888642464165:role/s3Redshift_readOnly' 
-- FORMAT AS PARQUET;

-- GRANT USAGE ON SCHEMA st_aux to aws_dev_red;
-- GRANT INSERT, SELECT, UPDATE, DELETE ON st_aux.st_trips_aux TO aws_dev_red;