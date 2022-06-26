import sys
from datetime import datetime
from .aws_athena_conf import athena_insert, athena_trunc, athena_select_qry

s3_output_location = 's3://bckt-dev/dev_log/athena/'
bucket_raw = 'raw-bckt-st'
bucket_stg = 'anltcs-bckt-st'
S3_REGION_NAME = 'us-east-1'

def prcss_bucket_definition(tbl_schm: str) -> str:
    '''
        prcss_bucket_definition String
        @type tbl_schm  String
        Assing the type of bucket base on table schema, and return the bucket name
    '''
    if tbl_schm.upper() == 'ST_RAW':
        return bucket_raw
    elif tbl_schm.upper() == 'STAGE':
        return bucket_stg

def prcss_insrt_athn(prttn_dt, prfx_bckt, qry_file, tbl_typ):
    '''
        prcss_insrt_athn    String
        @type prttn_dt      str
        @type prfx_bckt     str
        @type qry_file      str
        @type trnct_prtn    str
        @type tbl_typ       str

    '''
    try:
        bucket_nm = prcss_bucket_definition(tbl_typ)
        prfx_bckt = prfx_bckt.replace('{prttn_dt}', prttn_dt)
        my_oprtn = athena_insert(s3_output_location, S3_REGION_NAME, bucket_nm, prfx_bckt, qry_file, prttn_dt, False)

        return my_oprtn
    except BaseException as error:
        print('An exception ocurred: {0}'.format(error))
        return False

def prcss_trnc_athena(prttn_dt, prfx_bckt, tbl_typ):
    '''
        prcss_trnc_athena   String
        @type prttn_dt  str
        @type prfx_bckt str
        @type tbl_typ   str
        Remove objects from S3 bucket.
    '''
    try:
        bucket_nm = prcss_bucket_definition(tbl_typ)
        prfx_bckt = prfx_bckt.replace('{prttn_dt}', prttn_dt)
        
        my_oprtn = athena_trunc(bucket_nm, prfx_bckt)
        return my_oprtn
    except BaseException as error:
        print('An exception ocurred: {0}'.format(error))
        return False

