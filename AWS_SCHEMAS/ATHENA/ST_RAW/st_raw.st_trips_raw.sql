-- CREATE DATABASE st_raw;

CREATE EXTERNAL TABLE st_raw.st_trips_raw(
    st_region           STRING,
    origin_coord        STRING,
    destination_coord   STRING,
    st_datetime         TIMESTAMP,
    st_datasource       STRING
)
ROW FORMAT DELIMITED
FIELDS TERMINATED BY ','
LINES TERMINATED BY '\n'
STORED AS TEXTFILE
LOCATION 's3://raw-bckt-st/st_raw/st_trips_raw/'
TBLPROPERTIES ("skip.header.line.count"="1");

-- SELECT COUNT(1) FROM st_raw.st_trips_raw;