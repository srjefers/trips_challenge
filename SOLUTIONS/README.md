# Solutions
## Solution 1
There must be an automated process to ingest and store the data.
> This was solved by implementing Apache Nifi.
## Solution 2
Trips with similar origin, destination, and time of day should be grouped together.
> At the moment when is cleaning the data it groups the values at the same time, moving not duplicated data to the stage schema.
```sql
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
```
## Solution 3
Develop a way to inform the user about the status of the data ingestion without using a polling solution.
> Apache Airflow, has the option to send mails when some process of the Pipeline has been failing.

## Solution 4
The solution should be scalable to 100 million entries. It is encouraged to simplify the data by a data model. Please add proof that the solution is scalable.
> The architecture of apachen nifi in combination with athena, gives the chace to scale the entriens as much as the model needs, simplifing the data ingestion and the data cleaing with an AWS S3 Data Lake.

## Querys Redshift

### Query 1
Develop a way to obtain the weekly average number of trips for an area, defined by a bounding box (given by coordinates) or by a region.
```sql
SELECT 
	DATE_TRUNC('week', st_datetime) week, st_region, COUNT(1) trips 
FROM stage.st_trips
GROUP BY DATE_TRUNC('week', st_datetime), st_region;
```

### Query 2
From the two most commonly appearing regions, which is the latest datasource?
```sql

```

### Query 3
What regions has the "cheap_mobile" datasource appeared in?
```sql
SELECT DISTINCT st_region 
FROM stage.st_trips
WHERE st_datasource = 'cheap_mobile';
```