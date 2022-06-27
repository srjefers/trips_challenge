# Data Engineering Challenge

## Summary
This repository presents a solution to the Data Engineering Challenge provided by Jobsity, providing a broad explanation of how the problem was addressed and how a solution was given which was implemented in the AWS cloud. In this repository u can find all the scripts and schemas to build in by yourself. At the same time some few suggestions about another architecture that can be much better than the implemented in this project.
## Implemented architecture on AWS
In this project, the implementation of a fast data lake was carried out.

* For Data Ingestion, an Apache Nifi has been used, in an AWS EC2 instance.
* For Data Processing, a Python script has been implemented, which makes use of AWS athena, thus allowing a faster execution of data cleaning.
* For Data Warehousing, a AWS Redshift instances has been used, moving analytics data from AWS S3 to Redshift by `COPY` command

## Requirements and How to?
To build this proyect by yourself, 

### AWS Account with the next services
|AWS Service|# Instances|
|---|---:|
|AWS Athena|1 Instance|
|AWS Redshift|1 Cluser|
|AWS S3|3 Buckets|
|AWS EC2|2 Instances|

## Possible Issues