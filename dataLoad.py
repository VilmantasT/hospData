# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import sqlite3

conn = sqlite3.connect('hospitalData.sqlite')

cur = conn.cursor()

cur.executescript('''
    CREATE TABLE IF NOT EXISTS amb_detali
    (id INTEGER NOT NULL UNIQUE AUTOINCREMENT, laikotarpis TEXT, pasl_kodas INTEGER, balo_verte INTEGER, baz_kaina_balais NUMERIC, pac_skaicius NUMERIC, apm_pasl_skaicius INTEGER, suma_balais NUMERIC, suma_eurais NUMERIC);
    
    CREATE TABLE IF NOT EXISTS paslaugos (id INTEGER NOT NULL UNIQUE AUTOINCREMENT, pasl_kodas INTEGER, pasl_pavadinimas TEXT)
    
    CREATE TABLE IF NOT EXISTS gydytojai (id INTEGER NOT NULL UNIQUE AUTOINCREMENT, spaudo_nr NUMERIC UNIQUE, vardas TEXT, pavarde TEXT)
                  ''')
                  
