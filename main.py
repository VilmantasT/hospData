# -*- coding: utf-8 -*-
"""
Spyder Editor

File for tables creation and data loading to sqlite3 database from csv and pdf files.
"""
# import sys
# sys.path.insert(1, 'Loaders')
import sqlite3
import dataLoadManager

conn = sqlite3.connect('hospitalData.sqlite')

cur = conn.cursor()

cur.executescript('''
    CREATE TABLE IF NOT EXISTS amb_detali
    (id INTEGER NOT NULL PRIMARY KEY, laikotarpis TEXT, pasl_kodas INTEGER, balo_verte REAL, baz_kaina_balais REAL, pac_skaicius INTEGER, apm_pasl_skaicius INTEGER, suma_balais REAL, suma_eurais REAL);

    CREATE TABLE IF NOT EXISTS paslaugos (id INTEGER PRIMARY KEY NOT NULL, pasl_kodas INTEGER, pasl_pavadinimas TEXT, UNIQUE( pasl_kodas, pasl_pavadinimas));

    CREATE TABLE IF NOT EXISTS current_prices (id INTEGER PRIMARY KEY NOT NULL, service INTEGER, point_value REAL, price_in_points REAL, FOREIGN KEY(service) REFERENCES paslaugos(id));

    CREATE TABLE IF NOT EXISTS gydytojai (id INTEGER PRIMARY KEY NOT NULL, spaudo_nr NUMERIC UNIQUE, pavarde TEXT, UNIQUE(spaudo_nr, pavarde));

    CREATE TABLE IF NOT EXISTS ziniarastis (id INTEGER NOT NULL PRIMARY KEY, paslauga INTEGER, specialistas INTEGER, viso_apsilan INTEGER, viso_123_be_N INTEGER, del_ligos_L INTEGER, profilak_Pr INTEGER, mokami_is_viso INTEGER, mokami_is_ju_Pr INTEGER, kons_viso INTEGER, kons_be_siun INTEGER, kons_del_disp INTEGER, kons_but_pag INTEGER, data DATE, tlk TEXT, FOREIGN KEY(paslauga) REFERENCES paslaugos(id), FOREIGN KEY(specialistas) REFERENCES gydytojai(id));

    CREATE TABLE IF NOT EXISTS tmp_ziniarastis (id INTEGER NOT NULL PRIMARY KEY, paslauga INTEGER, specialistas INTEGER, viso_apsilan INTEGER, viso_123_be_N INTEGER, del_ligos_L INTEGER, profilak_Pr INTEGER, mokami_is_viso INTEGER, mokami_is_ju_Pr INTEGER, kons_viso INTEGER, kons_be_siun INTEGER, kons_del_disp INTEGER, kons_but_pag INTEGER, data DATE, tlk TEXT, FOREIGN KEY(paslauga) REFERENCES paslaugos(id), FOREIGN KEY(specialistas) REFERENCES gydytojai(id));

    CREATE TABLE IF NOT EXISTS suvestin_groups (id INTEGER NOT NULL PRIMARY KEY, code TEXT, service TEXT);

    CREATE TABLE IF NOT EXISTS amb_suvestine (id INTEGER NOT NULL PRIMARY KEY, service TEXT, service_count INTEGER, sum_points REAL, sum_euros REAL, data DATE, tlk TEXT, FOREIGN KEY(service) REFERENCES suvestin_groups(id));

    CREATE TABLE IF NOT EXISTS stat_suvestine (id INTEGER NOT NULL PRIMARY KEY, service_group TEXT, service_count INTEGER, bed_days INTEGER, sum_points REAL, sum_euros REAL, data DATE, tlk TEXT, FOREIGN KEY(service_group) REFERENCES suvestin_groups(id));

    CREATE TABLE IF NOT EXISTS tmp_stat_suvestine (id INTEGER NOT NULL PRIMARY KEY, service_group TEXT, service_count INTEGER, bed_days INTEGER, sum_points REAL, sum_euros REAL, data DATE, tlk TEXT, FOREIGN KEY(service_group) REFERENCES suvestin_groups(id));

    CREATE TABLE IF NOT EXISTS drg_groups (id INTEGER NOT NULL PRIMARY KEY, drg_code TEXT, drg_name TEXT);

    CREATE TABLE IF NOT EXISTS drg_ataskaita(id INTEGER NOT NULL PRIMARY KEY, balo_verte REAL, drg_kaina_eurais REAL, service_date DATE, drg INTEGER, average_price REAL, cards_num INTEGER, hosp_num INTEGER, drg_price_points REAL, tlk TEXT, FOREIGN KEY(drg) REFERENCES drg_groups(id))
                  ''')

print("HOSPITAL*DATA".center(50))
print("What do you want to do? (press a number):")
print("1. Upload data.")
print("2. Visualize Data")

action = input("Enter a number:")
print(action, type(action))

if action == '1':
    dataLoadManager.dataLoader(conn, cur)
elif action == '2':
    pass
conn.close()
