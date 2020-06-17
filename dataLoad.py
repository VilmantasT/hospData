# -*- coding: utf-8 -*-
"""
Spyder Editor

File for tables creation and data loading to sqlite3 database from csv and pdf files.
"""

import sqlite3
import csv
import datetime

conn = sqlite3.connect('hospitalData.sqlite')

cur = conn.cursor()

cur.executescript('''
    CREATE TABLE IF NOT EXISTS amb_detali
    (id INTEGER NOT NULL PRIMARY KEY, laikotarpis TEXT, pasl_kodas INTEGER, balo_verte INTEGER, baz_kaina_balais NUMERIC, pac_skaicius NUMERIC, apm_pasl_skaicius INTEGER, suma_balais NUMERIC, suma_eurais NUMERIC);
    
    CREATE TABLE IF NOT EXISTS paslaugos (id INTEGER PRIMARY KEY NOT NULL, pasl_kodas INTEGER, pasl_pavadinimas TEXT);
    
    CREATE TABLE IF NOT EXISTS gydytojai (id INTEGER NOT NULL PRIMARY KEY, spaudo_nr NUMERIC UNIQUET, pavarde TEXT);
    
    CREATE TABLE IF NOT EXISTS ziniarastis (id INTEGER NOT NULL PRIMARY KEY, paslauga TEXT, specialistas TEXT, viso_apsilan INTEGER, viso_123_be_N INTEGER, del_ligos_L INTEGER, profilak_Pr INTEGER, mokami_is_viso INTEGER, mokami_is_ju_Pr INTEGER, kons_viso INTEGER, kons_be_siun INTEGER, kons_del_disp INTEGER, kons_but_pag INTEGER, data DATE, tlk TEXT)
                  ''')
 
def loadZiniarastis():
    file = open(input('Enter file name: '))
    fileReader = csv.reader(file)
    fileLength = len(list(fileReader))

    file.seek(0)
    
    lastRowDate = list(fileReader)[-1][2].split(';')[1].split('-')
    date = datetime.date(int(lastRowDate[0]), int(lastRowDate[1]), int(lastRowDate[2]))


     
    file.seek(0)
    fileReader = csv.reader(file)

    
    for row in fileReader:
     
        if fileReader.line_num == 1 or fileReader.line_num > fileLength - 2:
            continue
        else:
            rowData = row[0].split(';')
            pasl_kodas = rowData[0].split()[0]
   
            pasl_pav = rowData[0].split()[1]
            
            cur.execute('SELECT id FROM paslaugos WHERE pasl_kodas = ?', (pasl_kodas,))
            if cur.fetchone() is None:
                cur.execute('INSERT INTO paslaugos (pasl_kodas, pasl_pavadinimas) VALUES (?, ?)', (pasl_kodas, pasl_pav))
                
                print('Inserted in paslaugos table ' + pasl_kodas + ' '+ pasl_pav)
    conn.commit()
loadZiniarastis() 
conn.close()
