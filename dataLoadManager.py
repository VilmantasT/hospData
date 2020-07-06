# -*- coding: utf-8 -*-
"""
Spyder Editor

File for tables creation and data loading to sqlite3 database from csv and pdf files.
"""
import loadZiniarastis

def dataLoader(conn, cur):
    print()
    print()
    print("From what source you want to upload data?".rjust(5))
    choice = input("Enter 1 - Upload from Ziniarastis; 2 - Upload from Detali")

    if choice == '1':
        loadZiniarastis.loadZiniarastis(conn, cur)
    elif choice == '2':
        loadDetali()
    else:
        print("Please enter a numer 1 or 2")
