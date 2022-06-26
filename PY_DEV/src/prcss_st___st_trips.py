import sys 
from datetime import datetime
from methods.prcss_orchestator import prcss_insrt_athn, prcss_trnc_athena, prcss_insrt_rdshft

def main(prttn_dt):
    '''
    '''
    try:
        folder_nm = 'stage/st_trips/'
        tbl_nm = 'st_trips'
        tbl_schm = 'stage'
        prttn_fld = 'prttn_dt'
        tbl_typ = 'stage'

        prttn_folder = prttn_fld + '={prttn_dt}'
        prfx_bckt = folder_nm + prttn_folder

        directory_sql = './sqlScripts/{0}/qry_{1}.{2}.sql'.format(tbl_schm, tbl_typ, tbl_nm)

        print('>> Truncate Partition')
        athena_truncate_stts = prcss_trnc_athena(str(prttn_dt), prfx_bckt, tbl_typ)
        print('>> Truncate STTS: {0}'.format(athena_truncate_stts))

        print('>> Insert Athena')
        athena_insrt_stts = prcss_insrt_athn(str(prttn_dt), prfx_bckt, directory_sql, tbl_typ)
        print('>> Athena STTS: {0}'.format(athena_insrt_stts))

        print('>> Insert Redshift')
        redshift_insrt_stts = prcss_insrt_rdshft(str(prttn_dt), prfx_bckt, tbl_schm, tbl_nm, prttn_fld)
        print('>> Redshift STTS: {0}'.format(redshift_insrt_stts))

    except BaseException as error:
        print('An exception ocurred: {0}'.format(str(error)))
    finally:
        print('END')

if __name__ == '__main__':
    main(sys.argv[1])
        