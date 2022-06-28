# Data Engineering Challenge

## Summary
This repository presents a solution to the Data Engineering Challenge provided by Jobsity, providing a broad explanation of how the problem was addressed and how a solution was given which was implemented in the AWS cloud. In this repository u can find all the scripts and schemas to build in by yourself. At the same time some few suggestions about another architecture that can be much better than the implemented in this project.
## Implemented architecture on AWS
<p align="center">
    <img width="700" alt="Alacritty Logo" src="https://raw.githubusercontent.com/srjefers/trips_challenge/main/ARCHITECTURE/Arquitectura_implementada.jpg">
</p>

In this project, the implementation of a fast data lake was carried out.

* For *Data Ingestion*, an Apache Nifi has been used, in an AWS EC2 instance.
* For *Data Processing*, a Python script has been implemented, which makes use of AWS athena, thus allowing a faster execution of data cleaning.
* For *Data Warehousing*, a AWS Redshift instances has been used, moving analytics data from AWS S3 to Redshift by `COPY` command

## Requirements and How to?
To build this proyect by yourself, you can just run the python script to move the data from RAW s3 to Redshift, for this u will need to install all the dependecies in the requirements.txt file. Python3 is needed for the execution of this project.

```
pip3 install /PY_DEV/requirements.txt
```

You can build this proyect in AWS, you will need those services:

### AWS Account with the next services
|AWS Service|# Instances|
|---|---:|
|AWS Athena|1 Instance|
|AWS Redshift|1 Cluser|
|AWS S3|3 Buckets|
|AWS EC2|2 Instances|
|AWS Secrets Manager|1 instance|

## Project layout

    ├─ AIRFLOW/         Dag automation
    ├─ ARCHITECTURE/    Graphic and more explination about AWS Architecture (see ARCHITECTURE/README.md)
    ├─ AWS_SCHEMAS/     SQL AWS Schemas
    │  ├─ ATHENA/       Athena SQL Table Schemas, ST_RAW/STAGE
    │  └─ REDSHIFT/     Redshift SQL Table Schemas, ST_AUX/STAGE
    ├─ PY_DEV/src/      Python proyect (see PY_DEV/README.md)
    |   ├─ methods/     Objects and Classes for connection and data manipulation
    |   └─ sqlScripts/  SQL Scripts
    └─ NIFI/            Nifi XML Flow


> ## Possible Issues 
> To get the auth from AWS Redshift in the python script, I have been using AWS Secrets Manager, and it can make some troubles when u where executing this part of the script.