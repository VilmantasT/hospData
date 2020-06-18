# -*- coding: utf-8 -*-
"""
Spyder Editor

File for tables creation and data loading to sqlite3 database from csv and pdf files.
"""

import sqlite3
import csv
import datetime
import re
import codecs

conn = sqlite3.connect('hospitalData.sqlite')

cur = conn.cursor()

cur.executescript('''
    CREATE TABLE IF NOT EXISTS amb_detali
    (id INTEGER NOT NULL PRIMARY KEY, laikotarpis TEXT, pasl_kodas INTEGER, balo_verte INTEGER, baz_kaina_balais NUMERIC, pac_skaicius NUMERIC, apm_pasl_skaicius INTEGER, suma_balais NUMERIC, suma_eurais NUMERIC);

    CREATE TABLE IF NOT EXISTS paslaugos (id INTEGER PRIMARY KEY NOT NULL, pasl_kodas INTEGER, pasl_pavadinimas TEXT);

    CREATE TABLE IF NOT EXISTS gydytojai (id INTEGER PRIMARY KEY NOT NULL, spaudo_nr NUMERIC UNIQUET, pavarde TEXT);

    CREATE TABLE IF NOT EXISTS ziniarastis (id INTEGER NOT NULL PRIMARY KEY, paslauga TEXT, specialistas TEXT, viso_apsilan INTEGER, viso_123_be_N INTEGER, del_ligos_L INTEGER, profilak_Pr INTEGER, mokami_is_viso INTEGER, mokami_is_ju_Pr INTEGER, kons_viso INTEGER, kons_be_siun INTEGER, kons_del_disp INTEGER, kons_but_pag INTEGER, data DATE, tlk TEXT)
                  ''')

def loadZiniarastis():
    file = codecs.open(input('Enter file name: '), encoding='ISO-8859-13')
    fileReader = csv.reader(file)
    fileLength = len(list(fileReader))

    file.seek(0)
    tlk = (list(fileReader)[-1][0].split(";")[0])

    
    file.seek(0)
    lastRowDate = list(fileReader)[-1][2].split(';')[1].split('-')
   
    date = datetime.date(int(lastRowDate[0]), int(lastRowDate[1]), int(lastRowDate[2]))

    file.seek(0)
    fileReader = csv.reader(file)


    for row in fileReader:

        if fileReader.line_num == 1 or fileReader.line_num > fileLength - 2:
            continue
        else:
         
            rowData = ",".join(row).replace(',', ' ').split(';')
        
            pasl_kodas = re.compile(r'(\d\d\d\d)').search(rowData[0]).groups()[0]
  
            pasl_id = cur.execute('SELECT id FROM paslaugos WHERE pasl_kodas = ?', (pasl_kodas,)).fetchone()
    
            if pasl_id is None:              
                pasl_pav = re.compile(r'(\D+)').search(rowData[0]).groups()[0]

                
                cur.execute('INSERT INTO paslaugos (pasl_kodas, pasl_pavadinimas) VALUES (?, ?)', (pasl_kodas, pasl_pav))

                print('Inserted in paslaugos table ' + pasl_kodas + ' '+ pasl_pav)

                conn.commit()
                pasl_id = cur.execute('SELECT id FROM paslaugos WHERE pasl_kodas = ?', (pasl_kodas,)).fetchone()
                
                
            spaudo_nr = re.compile(r'(\d+)').search(rowData[1]).groups()[0]         

            spec_id = cur.execute('SELECT id FROM gydytojai WHERE spaudo_nr =?', (spaudo_nr,)).fetchone()
            

            if spec_id is None:
                
                dr_surname = re.compile(r'(\D+)').search(rowData[1]).groups()[0]
                
                cur.execute('INSERT INTO gydytojai (spaudo_nr, pavarde) VALUES (?, ?)', (spaudo_nr, dr_surname))

                print('Inserted in gydytojai table ' + spaudo_nr + ' '+ dr_surname)
                
                conn.commit()
                spec_id = cur.execute('SELECT id FROM paslaugos WHERE pasl_kodas = ?', (pasl_kodas,)).fetchone()
            
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
            
            cur.execute("INSERT INTO ziniarastis(paslauga, specialistas, viso_apsilan, viso_123_be_N, del_ligos_L, profilak_Pr, mokami_is_viso, mokami_is_ju_Pr, kons_viso, kons_be_siun, kons_del_disp, kons_but_pag, data, tlk) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (pasl_id, spec_id, all_visits, all_123_w_N, for_illness_L, profil_Pr, all_payed, profil_from_payed, all_consult, consult_w_disp, consult_for_dispan, consult_for_emerg, date, tlk))
            # try:
            #     cur.execute("INSERT INTO ziniarastis(paslauga, specialistas, viso_apsilan, viso_123_be_N, del_ligos_L, profilak_Pr, mokami_is_viso, mokami_is_ju_Pr, kons_viso, kons_be_siun, kons_del_disp, kons_but_pag, data, vlk) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (pasl_id, spec_id, all_visits, all_123_w_N, for_illness_L, profil_Pr, all_payed, profil_from_payed, all_consult, consult_w_disp, consult_for_dispan, consult_for_emerg))
            # except:
            #     print("Something went wrong")

    #conn.commit()
loadZiniarastis()
conn.close()
