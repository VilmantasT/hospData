# -*- coding: utf-8 -*-
"""
Spyder Editor

File for tables creation and data loading to sqlite3 database from csv and pdf files.
"""
import sys
sys.path.insert(1, 'Loaders')

import loadZiniarastis
import loadDetali
import loadAmbSuvestine
import loadStatSuvestine
import loadDRG

def dataLoader(conn, cur):
    print("From what source you want to upload data?")
    raportChoice = input("Enter 1 - Upload from Ziniarastis; 2 - Upload from Detali; 3 - Upload from ambulatory Suvestine; 4 - Uload from stationary Suvestine")

    if raportChoice == '1':
        newsChoice = input("Enter 1 - Upload newsRaport with temporary data; 2 - Upload newsRaport with permanent data ")
        if newsChoice == '1':
            loadZiniarastis.loadZiniarastis(conn, cur, 'temp')
        elif newsChoice == '2':
            loadZiniarastis.loadZiniarastis(conn, cur, 'perm')
    elif raportChoice == '2':
        loadDetali.loadDetali(conn, cur)
    elif raportChoice == '3':
        loadAmbSuvestine.loadAmbSuvestine(conn, cur)
    elif raportChoice == '4':
        suvChoice = input("Enter 1 - Upload suvestine with temporary data; 2 - Upload suvestine with permanent data ")
        if suvChoice == '1':
            loadStatSuvestine.loadStatSuvestine(conn,cur, 'temp')
        elif suvChoice == '2':
            loadStatSuvestine.loadStatSuvestine(conn,cur, 'perm')
    elif raportChoice == '5':
        loadDRG.loadDRG(conn, cur)
    else:
        print("Please enter a number 1 or 4")
