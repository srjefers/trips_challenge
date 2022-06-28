INSERT INTO stage.st_trips 
    (st_region,origin_coord_east, origin_coord_nort, destination_coord_east, destination_coord_nort,st_datetime,st_datasource, prttn_dt)
SELECT 
    st_region,
    CAST(CASE 
        WHEN origin_coord IS NOT NULL THEN SPLIT(SUBSTR(origin_coord,STRPOS(origin_coord,'(')+1),' ')[1]
        ELSE null 
    END AS DOUBLE) origin_coord_east,
    CAST(CASE 
        WHEN origin_coord IS NOT NULL THEN REPLACE(SPLIT(SUBSTR(origin_coord,STRPOS(origin_coord,'(')+1),' ')[2], ')','')
        ELSE null 
    END AS DOUBLE) origin_coord_nort,
    CAST(CASE 
        WHEN destination_coord IS NOT NULL THEN SPLIT(SUBSTR(destination_coord,STRPOS(destination_coord,'(')+1),' ')[1]
        ELSE null 
    END AS DOUBLE) destination_coord_east,
    CAST(CASE 
        WHEN destination_coord IS NOT NULL THEN REPLACE(SPLIT(SUBSTR(destination_coord,STRPOS(destination_coord,'(')+1),' ')[2], ')','')
        ELSE null 
    END AS DOUBLE) destination_coord_nort,
    st_datetime,st_datasource,
    {prttn_dt} 
FROM (
    SELECT 
        st_region,origin_coord,destination_coord,st_datetime,st_datasource,
        ROW_NUMBER() OVER (PARTITION BY origin_coord, destination_coord, st_datetime ORDER BY st_datetime DESC) rn
    FROM st_raw.st_trips_raw
) tmp_tbl
WHERE rn = 1;