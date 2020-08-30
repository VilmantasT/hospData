from pathlib import Path
import codecs
import os
import csv
import re
import logging
import traceback

def loadDRG(conn, cur):
    # import pdb; pdb.set_trace()
    data_folder = Path("/media/vilmantas/BAD89498D894548B/Projektai/Ataskaitos/hospData/Files")

    file = input('Enter file name: ')

    file_to_open = data_folder / file

    file_name, file_extension = os.path.splitext(file)

    if file_extension == '.CSV':
        fileHandle = codecs.open(file_to_open, encoding='ISO-8859-13')
        fileReader = csv.reader(fileHandle)

    else:
        print("Bad file type!")

    fileLength = len(list(fileReader))

    fileHandle.seek(0)
    tlk = (list(fileReader)[-1][0].split(";")[0])

    fileHandle.seek(0)
    fileReader = csv.reader(fileHandle)

    for row in fileReader:

        if fileReader.line_num == 1 or fileReader.line_num > fileLength - 2:
            continue
        else:
            rowData = ",".join(row).replace(',', '.').split(';')

            point_value = rowData[0]
            drg_price_euros = rowData[1]
            service_date = rowData[2]
            drg_code = rowData[4]
            drg_name = rowData[5]
            average_price = rowData[6]
            cards_num = rowData[7]
            hosp_num = rowData[8]
            drg_price_points = rowData[9]

            drg_id = cur.execute("SELECT id FROM drg_groups WHERE drg_code =? AND drg_name = ?", (drg_code, drg_name)).fetchone()

            if drg_id is None:
                cur.execute('INSERT INTO drg_groups (drg_code, drg_name) VALUES (?, ?)', (drg_code, drg_name))

                print('Added DRG group.')

                conn.commit()

                drg_id = cur.execute("SELECT id FROM drg_groups WHERE drg_code =? AND drg_name = ?", (drg_code, drg_name)).fetchone()

            dataExists = cur.execute('SELECT id FROM drg_ataskaita WHERE drg =? AND service_date = ? AND tlk= ?', (drg_id[0], service_date, tlk)).fetchone()

            if dataExists is None:
                try:
                    cur.execute('INSERT INTO drg_ataskaita (balo_verte, drg_kaina_eurais, service_date, drg, average_price, cards_num, hosp_num, drg_price_points, tlk) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)', (point_value, drg_price_euros, service_date, drg_id[0], average_price, cards_num, hosp_num, drg_price_points, tlk))

                    print("Added to drg_ataskaita")
                    conn.commit()
                except Exception as e:
                    logging.error(traceback.format_exc())
            else:
                print("Data already exists. Continue")
                continue
