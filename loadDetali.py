import codecs
import csv
import re
import traceback
import logging
import sys
from addServiceAndSpecialist import addService, addSpecialist

def loadDetali(conn, cur):
    file = codecs.open(input('Enter file name: '), encoding='ISO-8859-13')
    fileReader = csv.reader(file)
    fileLength = len(list(fileReader))

    file.seek(0)
    fileReader = csv.reader(file)

    for row in fileReader:

        if fileReader.line_num < 7 or fileReader.line_num >= fileLength - 2:
            continue
        else:

            rowData = ','.join(row)

            extract = re.compile(r'(\d\d\d\d-\d\d).+;T;(\d\d\d\d;.+)')
            foundData = extract.search(rowData)
            try:
                serviceTime = foundData.group(1)
                listedData = foundData.group(2).split(";")

                serviceCode = listedData[0]

                serviceId = cur.execute('SELECT id FROM paslaugos WHERE pasl_kodas = ?', (serviceCode,)).fetchone()

                if serviceId is None:
                    print(listedData)

                    serviceName = listedData[1]
                    print("Name", serviceName)
                    serviceId = addService(conn, cur, serviceCode, serviceName)

                serviceValue = listedData[2]
                servicePrice = listedData[3]
                patientsCount = listedData[4]
                servicesCount = listedData[5]
                sumOfPoints = listedData[6]
                sumOfEuros = listedData[7]

                newData = [serviceTime, serviceId[0], serviceValue, servicePrice, patientsCount, servicesCount, sumOfPoints, sumOfEuros]


                dataExists = cur.execute('SELECT * FROM amb_detali WHERE laikotarpis = ? AND pasl_kodas = ?', (serviceTime, serviceId)).fetchone()
                #
                # except:
                #     dataExists = False
                print(dataExists)

                if dataExists:
                    oldData = list(dataExists)[3:]
                    newDataUpdate = newData[3:]

                    for i in range(len(newDataUpdate)):
                        if int(newDataUpdate[i]) != oldData[i]:

                            try:
                                cur.execute("UPDATE amb_detali SET balo_verte = ?, baz_kaina_balais=?, pac_skaicius=?, apm_pasl_skaicius=?, suma_balais=?, suma_eurais=? WHERE laikotarpis = ? AND pasl_kodas = ?", (serviceValue, servicePrice, patientsCount, servicesCount, sumOfPoints, sumOfEuros, serviceTime, serviceCode))

                                print("Record Updated!")

                                conn.commit()
                            except Exception as e:
                                logging.error(traceback.format_exc())
                        else:
                            print("Data identical. Continue")
                            continue

                elif not dataExists:

                    cur.execute('INSERT INTO amb_detali(laikotarpis, pasl_kodas, balo_verte, baz_kaina_balais, pac_skaicius, apm_pasl_skaicius, suma_balais, suma_eurais) VALUES(?,?,?,?,?,?,?,?)', (serviceTime, serviceId[0], serviceValue, servicePrice, patientsCount, servicesCount, sumOfPoints, sumOfEuros))

                    conn.commit()

                    print("Inserted into amb_detali")

            except:
                print("*************Bad line!**************************")
