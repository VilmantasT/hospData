# -*- coding: utf-8 -*-
"""
Spyder Editor

File for tables creation and data loading to sqlite3 database from csv and pdf files.
"""
import loadZiniarastis
import loadDetali

def dataLoader(conn, cur):
    print("From what source you want to upload data?")
    raportChoice = input("Enter 1 - Upload from Ziniarastis; 2 - Upload from Detali ")

    if raportChoice == '1':
        newsChoice = input("Enter 1 - Upload newsRaport with temporary data; 2 - Upload newsRaport with permanent data ")
        if newsChoice == '1':
            loadZiniarastis.loadZiniarastis(conn, cur, 'temp')
        elif newsChoice == '2':
            loadZiniarastis.loadZiniarastis(conn, cur, 'perm')
    elif choice == '2':
        loadDetali.loadDetali(conn, cur)
    else:
        print("Please enter a numer 1 or 2")
