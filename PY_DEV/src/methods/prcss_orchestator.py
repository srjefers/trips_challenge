import sys
from datetime import datetime
from .aws_athena_conf import athena_insert, athena_trunc, athena_select_qry
from .aws_redshift_conf import redshift_cnn

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

def prcss_insrt_athn(prttn_dt: str, prfx_bckt: str, qry_file: str, tbl_typ: str) -> str:
    '''
        prcss_insrt_athn    String
        @type prttn_dt      str
        @type prfx_bckt     str
        @type qry_file      str
        @type trnct_prtn    str
        @type tbl_typ       str
        Insert values in Athena, executing sql Script.
    '''
    try:
        bucket_nm = prcss_bucket_definition(tbl_typ)
        prfx_bckt = prfx_bckt.replace('{prttn_dt}', prttn_dt)
        my_oprtn = athena_insert(s3_output_location, S3_REGION_NAME, bucket_nm, prfx_bckt, qry_file, prttn_dt, False)

        return my_oprtn
    except BaseException as error:
        print('An exception ocurred: {0}'.format(error))
        return False

def prcss_trnc_athena(prttn_dt: str, prfx_bckt: str, tbl_typ: str) -> bool: 
    '''
        prcss_trnc_athena   Bool
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

def prcss_insrt_rdshft(prttn_dt: str, prfx_bckt: str, tbl_schm: str, tbl_rdshft: str, prttn_fld: str) -> str:
    '''
        prcss_insrt_rdshft  String
        @type prttn_dt      str
        @type prfx_bckt     str
        @type tbl_schm      str
        @type tbl_rdshft    str
        @type prttn_fld     str
        Insert the full process on redshift, from COPY to the analytics schema. 
    '''
    try:
        bucket_nm = prcss_bucket_definition(tbl_schm)

        conR = redshift_cnn()
        curR = conR.cursor()

        cp_rdshft = '''
                        COPY st_aux.{0}_aux
                        FROM 's3://{1}/{2}/' 
                        iam_role 'arn:aws:iam::888642464165:role/s3Redshift_readOnly' 
                        FORMAT AS PARQUET;
                    '''.format(tbl_rdshft, bucket_nm, prfx_bckt)

        cp_rdshft = cp_rdshft.replace('{prttn_dt}', prttn_dt)
        dlt_aux = 'DELETE FROM st_aux.{0}_aux'.format(tbl_rdshft)
        #print(cp_rdshft)
        #print(dlt_aux)
        curR.execute(dlt_aux)
        #print('dlt_aux done')
        curR.execute(cp_rdshft)

        dlt_tbl_prttn_dt = "DELETE FROM {0}.{1} WHERE prttn_dt = TO_TIMESTAMP('{2}', 'yyyyMMdd'); commit;".format(tbl_schm, tbl_rdshft, prttn_dt)
        #print(dlt_tbl_prttn_dt)
        curR.execute(dlt_tbl_prttn_dt)

        insrt_qry = """
                        INSERT INTO {0}.{1}
                        SELECT *, TO_TIMESTAMP('{2}', 'yyyyMMdd')
                        FROM st_aux.{1}_aux;
                        COMMIT;
                    """.format(tbl_schm, tbl_rdshft, prttn_dt)

        #print(insrt_qry)
        curR.execute(insrt_qry)
        conR.commit()
        return 'Redshift Succesfully completed'
    except BaseException as error:
        print('An exception ocurred in redshift insert: {0}'.format(str(error)))
    finally:
        curR.close()
        conR.close()
    