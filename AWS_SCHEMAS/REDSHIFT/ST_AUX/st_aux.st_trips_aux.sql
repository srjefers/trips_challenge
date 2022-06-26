-- CREATE DATABASE analytics_db;
-- CREATE SCHEMA st_aux;

CREATE TABLE st_aux.st_trips_aux(
    st_region           VARCHAR(300),
    origin_coord        VARCHAR(300),
    destination_coor    VARCHAR(300),
    st_datetime         TIMESTAMP,
    st_datasource       VARCHAR(300)
)


-- COPY st_aux.st_trips_aux 
-- FROM 's3://anltcs-bckt-st/stage/st_trips/prttn_dt=20220626/' 
-- iam_role 'arn:aws:iam::888642464165:role/s3Redshift_readOnly' 
-- FORMAT AS PARQUET;