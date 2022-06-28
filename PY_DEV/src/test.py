from prcss_st___st_trips import main as trips_main

ENV = 'TEST'
if ENV == 'TEST':
    fechas = [20220626]
    for fecha in fechas:
        trips_main(1,fecha)
        trips_main(2,fecha)