# PY_DEV

## Summary
The python script contemplates the cleaning and processing of the data.

## Execute
Python scripts contemplates the use of data partitioning, for this u need to change the date for execution on the test file. And change the name of the file `prcss_st.st_trips.py` to `prcss_st___st_trips.py`. This is only for testing porpuses.
```
python3 test.py
```

## Docker
`Dockerfile` file with code to conteinerize the solution.

## Requirements.txt
File with all the dependencies. To install the dependencies execute:
```
pip3 install /PY_DEV/requirements.txt
```

## src/methods
Contains all the objects and classes to connect with aws athena and aws redshift. And process data.

## src/sqlScripts
Contains SQL scripts to be executed in AWS Athena, to clean data and move data from ST_RAW to STAGE schema.