import codecs
import csv
import os
import re
import traceback
import logging
from pathlib import Path


def loadStatSuvestine(conn, cur, dTime):
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

    dataTable = 'stat_suvestine'

    if dTime != 'perm':
        cur.execute("DELETE FROM tmp_stat_suvestine")
        conn.commit()
        dataTable = 'tmp_stat_suvestine'

    fileHandle.seek(0)
    tlk = (list(fileReader)[-1][0].split(";")[0])

    fileHandle.seek(0)
    date = re.compile(r'(\d\d\d\d-\d\d)').search(''.join(list(fileReader)[-1])).groups()[0]

    fileHandle.seek(0)
    fileReader = csv.reader(fileHandle)

    for row in fileReader:
        rowData = ",".join(row).replace(',', '.').split(';')

        if fileReader.line_num == 1 or fileReader.line_num > fileLength - 2:
            continue
        else:
            code = re.compile(r'(\d.\d*)').search(rowData[0]).groups()[0]
            service_name = re.compile(r'\s(.+)').search(rowData[0]).groups()[0]

            service_id = cur.execute('SELECT * FROM suvestin_groups WHERE code = ? AND service = ?', (code, service_name)).fetchone()

            if service_id is None:
                cur.execute('INSERT INTO suvestin_groups (code, service) VALUES (?, ?)', (code, service_name))

                conn.commit()

                service_id = cur.execute('SELECT * FROM suvestin_groups WHERE code = ? AND service = ?', (code, service_name)).fetchone()

            service_count = rowData[1]
            bed_days_count = rowData[2]
            sum_points = rowData[3]
            sum_euros = rowData[4]

            dataExists = cur.execute('SELECT * FROM ' + dataTable + ' WHERE service_group =? AND data = ? AND tlk= ?', (int(service_id[0]), date, tlk)).fetchone()

            if dataExists is None:
                try:
                    cur.execute("INSERT INTO "+ dataTable + " (service_group, service_count, bed_days, sum_points, sum_euros, data, tlk) VALUES (?, ?, ?, ?, ?, ?, ?)", (int(service_id[0]), service_count, bed_days_count, sum_points, sum_euros, date, tlk))

                    print("Added to " + dataTable)
                    conn.commit()
                except Exception as e:
                        logging.error(traceback.format_exc())
            else:
                print("Data already exists. Continue")
                continue
