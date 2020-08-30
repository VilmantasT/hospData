import codecs
import csv
import re
import traceback
from pathlib import Path
import logging
import sys
import datetime
from addServiceAndSpecialist import addService, addSpecialist

def loadDetali(conn, cur):

    data_folder = Path("/media/vilmantas/BAD89498D894548B/Projektai/Ataskaitos/hospData/Files")

    file = input('Enter file name: ')

    # file_name, file_extension = os.path.splitext(file)

    file_to_open = data_folder / file
    print(file_to_open)


    file = codecs.open(file_to_open, encoding='ISO-8859-13')
    fileReader = csv.reader(file)
    fileLength = len(list(fileReader))

    file.seek(0)
    fileReader = csv.reader(file)

    for row in fileReader:

        if fileReader.line_num < 7 or fileReader.line_num >= fileLength - 2:
            continue
        else:

            rowData = '.'.join(row)

            extract = re.compile(r'(\d\d\d\d-\d\d).+;T;(\d\d\d\d;.+)')
            foundData = extract.search(rowData)
            try:
                serviceTime = foundData.group(1)
                listedData = foundData.group(2).split(";")

                serviceCode = listedData[0]

                serviceId = cur.execute('SELECT id FROM paslaugos WHERE pasl_kodas = ?', (serviceCode,)).fetchone()

                if serviceId is None:

                    serviceName = listedData[1]
                    serviceId = addService(conn, cur, serviceCode, serviceName)

                serviceValue = listedData[2]
                servicePrice = listedData[3]
                patientsCount = listedData[4]
                servicesCount = listedData[5]
                sumOfPoints = listedData[6]
                sumOfEuros = listedData[7]

                try:

                    serviceOldPrice =  cur.execute('SELECT point_value, price_in_points FROM current_prices WHERE service = ?', (serviceId)).fetchone()
                    if not serviceOldPrice:
                        cur.execute('INSERT INTO current_prices (service, point_value, price_in_points) VALUES (?, ?, ?)', (serviceId[0], serviceValue, servicePrice))

                        conn.commit()
                    elif serviceOldPrice[0] != serviceValue:
                        cur.execute('UPDATE current_prices SET point_value = ? WHERE service =?', (serviceValue, serviceId[0]))

                        conn.commit()

                    elif serviceOldPrice[1] != servicePrice:
                        cur.execute('UPDATE current_prices SET price_in_points = ? WHERE service =?', (servicePrice, serviceId[0]))

                        conn.commit()
                except Exception as e:
                    logging.error(traceback.format_exc())

                dataExists = cur.execute('SELECT * FROM amb_detali WHERE laikotarpis = ? AND pasl_kodas = ? AND balo_verte = ? AND baz_kaina_balais = ? AND pac_skaicius = ? AND apm_pasl_skaicius = ?', (serviceTime, serviceId[0], serviceValue, servicePrice, patientsCount, servicesCount)).fetchone()

                if not dataExists:
                    try:
                        cur.execute('INSERT INTO amb_detali(laikotarpis, pasl_kodas, balo_verte, baz_kaina_balais, pac_skaicius, apm_pasl_skaicius, suma_balais, suma_eurais) VALUES(?,?,?,?,?,?,?,?)', (serviceTime, serviceId[0], float(serviceValue), float(servicePrice), int(patientsCount), int(servicesCount), float(sumOfPoints), float(sumOfEuros)))

                        print("Inserted into amb_detali")
                        conn.commit()
                    except Exception as e:
                        logging.error(traceback.format_exc())


            except:
                print("*************Bad line!**************************")
                logging.error(traceback.format_exc())
