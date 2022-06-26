-- CREATE DATABASE stage;

CREATE EXTERNAL TABLE stage.st_trips(
    st_region           STRING,
    origin_coord        STRING,
    destination_coor    STRING,
    st_datetime         TIMESTAMP,
    st_datasource       STRING
)
PARTITIONED BY (prttn_dt BIGINT)
STORED AS PARQUET
LOCATION 's3://anltcs-bckt-st/stage/st_trips'
TBLPROPERTIES ("parquet.compression"="SNAPPY");

-- SELECT COUNT(1) FROM stage.st_trips;

--------
-- INSERT INTO stage.st_trips (st_region,origin_coord,destination_coor,st_datetime,st_datasource, prttn_dt)
-- SELECT st_region,origin_coord,destination_coor,st_datetime,st_datasource, 20220626 FROM st_raw.st_trips_raw;