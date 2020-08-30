import codecs
import csv
import os
import re
from pathlib import Path
import traceback
import logging
from addServiceAndSpecialist import addService, addSpecialist
import dumpDataToJson

def loadZiniarastis(conn, cur, dTime):

    data_folder = Path("/media/vilmantas/BAD89498D894548B/Projektai/Ataskaitos/hospData/Files")

    file = input('Enter file name: ')

    file_name, file_extension = os.path.splitext(file)

    file_to_open = data_folder / file
    print(file_to_open)

    if file_extension == '.CSV':
        fileHandle = codecs.open(file_to_open, encoding='ISO-8859-13')
        fileReader = csv.reader(fileHandle)
    else:
        print("Bad file type!")

    fileLength = len(list(fileReader))

    dataTable = 'ziniarastis'

    if dTime != 'perm':
        cur.execute("DELETE FROM tmp_ziniarastis")
        conn.commit()
        dataTable = 'tmp_ziniarastis'


    fileHandle.seek(0)
    tlk = (list(fileReader)[-1][0].split(";")[0])

    fileHandle.seek(0)
    date = list(fileReader)[-1][2].split(';')[2]

    fileHandle.seek(0)
    fileReader = csv.reader(fileHandle)

    for row in fileReader:

        if fileReader.line_num == 1 or fileReader.line_num > fileLength - 2:
            continue
        else:
            rowData = ",".join(row).replace(',', ' ').split(';')

            pasl_kodas = re.compile(r'(\d\d\d\d)').search(rowData[0]).groups()[0]

            pasl_id = cur.execute('SELECT id FROM paslaugos WHERE pasl_kodas = ?', (pasl_kodas,)).fetchone()

            if pasl_id is None:
                pasl_pav = re.compile(r'(\D+)').search(rowData[0]).groups()[0]

                pasl_id = addService(conn, cur, pasl_kodas, pasl_pav)

            spaudo_nr = re.compile(r'(\d+)').search(rowData[1]).groups()[0]

            spec_id = cur.execute('SELECT id FROM gydytojai WHERE spaudo_nr =?', (spaudo_nr,)).fetchone()

            if spec_id is None:

                dr_surname = re.compile(r'(\D+)').search(rowData[1]).groups()[0]

                spec_id = addSpecialist(conn, cur, spaudo_nr, dr_surname)

            all_visits = rowData[2]
            all_123_w_N = rowData[3]
            for_illness_L = rowData[4]
            profil_Pr = rowData[5]
            all_payed = rowData[9]
            profil_from_payed = rowData[10]
            all_consult = rowData[11]
            consult_w_disp = rowData[12]
            consult_for_dispan = rowData[13]
            consult_for_emerg = rowData[14]


            dataExists = cur.execute('SELECT * FROM '+ dataTable +' WHERE paslauga = ? AND specialistas = ? AND data = ? AND tlk = ?', (pasl_id[0], spec_id[0], date, tlk)).fetchone()

            if dataExists is None:
                try:
                    cur.execute("INSERT INTO "+dataTable+"(paslauga, specialistas, viso_apsilan, viso_123_be_N, del_ligos_L, profilak_Pr, mokami_is_viso, mokami_is_ju_Pr, kons_viso, kons_be_siun, kons_del_disp, kons_but_pag, data, tlk) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (pasl_id[0], spec_id[0], all_visits, all_123_w_N, for_illness_L, profil_Pr, all_payed, profil_from_payed, all_consult, consult_w_disp, consult_for_dispan, consult_for_emerg, date, tlk))

                    print("Added to "+dataTable)
                    conn.commit()
                except Exception as e:
                        logging.error(traceback.format_exc())
            else:
                print("Data already exists. Continue")
                continue
