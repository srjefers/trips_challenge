import psycopg2
import json
import boto3

def redshift_cnn():
    """
        redshift_cnn Connection Object
        Connect to redshift database using AWS Key management service
    """
    client = boto3.client('secretsmanager')
    response = client.get_secret_value(SecretId='dev/aws/redshift')
    secretDict = json.loads(response['SecretString'])
    con = psycopg2.connect(host=secretDict['host'],database='analytics_db',user=secretDict['username'],password=secretDict['password'],port=5439)

    con.autocommit = True

    return con

