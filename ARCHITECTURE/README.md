# ARCHITECTURE

## Implemented Architecture
<p align="center">
    <img width="700" alt="Alacritty Logo" src="https://raw.githubusercontent.com/srjefers/trips_challenge/main/ARCHITECTURE/Arquitectura_implementada.jpg">
</p>

### Summary
The data is extracted from an external server, through the use of apache nifi, apache nifi has been defined for its ease of implementation in sftp and for its tools to move a file from another server with good performance. As well as being a reactive tool which will extract either by schedule or reactively when detecting a change or a new file on the server.

These files are deposited in an aws s3 bucket, later read through aws athena, using a script which automates the execution of the reading of the raw bucket and its process towards a stage bucket, with processed and clean data. athena has been defined by its sql interface, which allows data to be read using SQL. 

This script was deployed on aws ecs with ecr, thus having container execution on aws. For its execution, aws mwaa has been used, which provides a "ready to deploy" instance of apache airflow, which will be an orchestrator of the script.

After its cleaning and the construction of an analytical model, the data is sent to aws redshift, a service which is used as a data warehouse for subsequent data analysis.

### Data Ingestion
Apache Nifi, an AWS EC2 instance with medium resources has been used to carry out the implementation of Apache Nifi. Apache NIFi has been chosen as SFTP, due to its easy implementation of data ingestion from an external data source, in addition to providing the ease of removing the files in an AWS S3 bucket, allows the constant reading of the directory in an external server, thus allowing to determine the changes that have been found in the directory of the external server and send it to AWS.

### Data Processing
Using AWS ECS instance, to deploy containerized python script. For this process, the architecture contemplates the use of AWS Athena, providen an SQL interface like Apache Hadoop that gives you the ability to work with data in SQL like HDFS. An reading data from AWS S3 bucket, ingested from Apache Nifi. Reading data from AWS S3 gives you the ability to work with many kinds of data files, and just needing to get those data files on AWS S3 bucket to be interpreted by Athena.

### Data Warehousing
With AWS Redshift, uses SQL to analyze structured and semi-structured data across data warehouses, operational databases, and data lakes, using AWS-designed hardware and machine learning to deliver the best price performance at any scale. 

### Other Services
> #### Amazon MWAA
> This service was implemented to have an instance with an apache airflow ready to be used and self-managed by aws, allowing the user to spend more time developing other activities.
> #### AWS Key Management Service
> AWS service used to store database credentials.


## Alternative Architecture
<p align="center">
    <img width="700" alt="Alacritty Logo" src="https://raw.githubusercontent.com/srjefers/trips_challenge/main/ARCHITECTURE/Arquitectura_alternativa.jpg">
</p>

> #### AWS Transfer Family
> AWS Transfer Family implementation would allow users to transfer files via a Filezilla connection to aws s3, should an implementation be required which would require "human intervention" to send files.
> #### AWS Lambda
> The implementation of an AWS Lambda provides a reactive architecture, which detecting a change in the bucket would execute the python script, allowing data to be obtained with less delay.
> #### Other cases
> Just implementing a python script in AWS ECS to read any kind of data source, such as sftp, rest api or getting directly from a database.