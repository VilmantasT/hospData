# -*- coding: utf-8 -*-
"""
Spyder Editor

File for tables creation and data loading to sqlite3 database from csv and pdf files.
"""

import sqlite3
import dataLoadManager
import PyPDF2

conn = sqlite3.connect('hospitalData.sqlite')

cur = conn.cursor()

cur.executescript('''
    CREATE TABLE IF NOT EXISTS amb_detali
    (id INTEGER NOT NULL PRIMARY KEY, laikotarpis TEXT, pasl_kodas INTEGER, balo_verte REAL, baz_kaina_balais REAL, pac_skaicius INTEGER, apm_pasl_skaicius INTEGER, suma_balais REAL, suma_eurais REAL);

    CREATE TABLE IF NOT EXISTS paslaugos (id INTEGER PRIMARY KEY NOT NULL, pasl_kodas INTEGER, pasl_pavadinimas TEXT, UNIQUE( pasl_kodas, pasl_pavadinimas));

    CREATE TABLE IF NOT EXISTS gydytojai (id INTEGER PRIMARY KEY NOT NULL, spaudo_nr NUMERIC UNIQUE, pavarde TEXT, UNIQUE(spaudo_nr, pavarde));

    CREATE TABLE IF NOT EXISTS ziniarastis (id INTEGER NOT NULL PRIMARY KEY, paslauga INTEGER, specialistas INTEGER, viso_apsilan INTEGER, viso_123_be_N INTEGER, del_ligos_L INTEGER, profilak_Pr INTEGER, mokami_is_viso INTEGER, mokami_is_ju_Pr INTEGER, kons_viso INTEGER, kons_be_siun INTEGER, kons_del_disp INTEGER, kons_but_pag INTEGER, data DATE, tlk TEXT, FOREIGN KEY(paslauga) REFERENCES paslaugos(id), FOREIGN KEY(specialistas) REFERENCES gydytojai(id));

    CREATE TABLE IF NOT EXISTS tmp_ziniarastis (id INTEGER NOT NULL PRIMARY KEY, paslauga INTEGER, specialistas INTEGER, viso_apsilan INTEGER, viso_123_be_N INTEGER, del_ligos_L INTEGER, profilak_Pr INTEGER, mokami_is_viso INTEGER, mokami_is_ju_Pr INTEGER, kons_viso INTEGER, kons_be_siun INTEGER, kons_del_disp INTEGER, kons_but_pag INTEGER, data DATE, tlk TEXT, FOREIGN KEY(paslauga) REFERENCES paslaugos(id), FOREIGN KEY(specialistas) REFERENCES gydytojai(id))
                  ''')

print("HOSPITAL*DATA".center(50))
print("What do you want to do? (press a number):".rjust(5))
print("1. Upload data.".rjust(5))
print("2. Update data.".rjust(5))
print("3. Get Data".rjust(5))

action = input("Enter a number:")

if action == '1':
    dataLoadManager.dataLoader(conn, cur)
elif action == '2':
    pass
conn.close()
