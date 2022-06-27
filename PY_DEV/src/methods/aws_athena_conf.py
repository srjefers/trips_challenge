import boto3
from pyathena import connect
from pyathena import DatabaseError

s3_output_location = 's3://bckt-dev/dev_log/athena/'
S3_REGION_NAME = 'us-east-1'

def athena_insert(s3_output_location: str, s3_region_name: str, bucket: str, prfx_bckt: str, qry_file: str, prttn_dt: str, prnt_qry: bool) -> bool:
    '''
        ATHENA INSERT String
        @type s3_output_location    str
        @type s3_region_name        str    
        @type bucket                str
        @type prfx_bckt             str
        @type qry_file              str
        @type prttn_dt              str
        @type prnt_qry              bool
        Insert values from st_raw schema to stage schema.
    '''
    try:
        f = open(qry_file)
        sql_qry = f.read()
        sql_qry = sql_qry.replace('{prttn_dt}', prttn_dt)

        if prnt_qry:
            print(sql_qry)

    except IOError:
        print('Error found in:', qry_file)
        raise

    try:
        cursor = connect(
                            duration_seconds=3600, 
                            output_location=s3_output_location, 
                            s3_staging_dir=s3_output_location,
                            region_name=s3_region_name
                        ).cursor()
        
        cursor.execute(sql_qry)
        return 'Query Succesfully executed'
    except DatabaseError as e:
        print('Error during athena execution... {0}'.format(str(e)))
        raise

def athena_trunc(bucket: str, prfx_bckt: str) -> bool:
    '''
        ATHENA_TRUNC    Bool
        @type bucket    str
        @type prfx_bckt str
        Remove objects from S3 bucket.
    '''
    try:
        s3_resource = boto3.resource('s3')

        bucket = s3_resource.Bucket(bucket)
        for obj in bucket.objects.filter(Prefix='{0}/'.format(prfx_bckt)):
            s3_resource.Object(bucket.name, obj.key).delete()
        return True
    except BaseException as error:
        print('An exception occurred: {0}'.format(error))
        return False

def athena_select_qry(sql_qry: str, prnt_qry: bool):
    '''
        ATHENA SELECT QRY
        @type sql_qry   str
        @type prnt_qry  bool
        Executes select query.
    '''
    if prnt_qry:
        print(sql_qry)
    
    cursor = connect(
                        duration_seconds=3600, 
                        output_location=s3_output_location, 
                        s3_staging_dir=s3_output_location,
                        region_name=s3_region_name
                    ).cursor()

    try:
        cursor.execute(sql_qry)

        metadata = cursor.description
        data = cursor.fetchall()

        return data, metadata
    
    except DatabaseError as e:
        print('Error generated ... {0}'.format(str(e)))
        raise