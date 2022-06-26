import psycopg2
import json
import boto3

def redshift_cnn():
    client = boto3.client('secretsmanager')
    response = client.get_secret_value(SecretId='dev/aws/redshift')
    secretDict = json.loads(response['SecretString'])
    con = psycopg2.connect(host=secretDict['host'],database='analytics_db',user=secretDict['username'],password=secretDict['password'],port=5439)

    con.autocommit = True

    return con

def redshift_exc_qry(sql_qry):
    con = redshift_cnn()
    cursor = con.cursor()
    cursor.execute(sql_qry)
    con.commit()
    cursor.close()

    con.close()
    return True

def redshift_exc_qry_file_prod(qry_file, prttn_dt, prnt_qry):
    with open(qry_file) as f:
        sql_qry = f.read()
        if prnt_qry == 'S':
            print(prnt_qry)
    
    sql_qry = sql_qry.replace('{prttn_dt}',prttn_dt)
    con = redshift_cnn()
    cursor = con.cursor()
    cursor.execute(sql_qry)
    con.commit()
    cursor.close()
    con.close()
    return True