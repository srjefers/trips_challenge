INSERT INTO stage.st_trips 
    (st_region,origin_coord,destination_coord,st_datetime,st_datasource, prttn_dt)
SELECT 
    st_region,origin_coord,destination_coord,st_datetime,st_datasource, {prttn_dt} 
FROM st_raw.st_trips_raw;