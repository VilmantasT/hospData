# -*- coding: utf-8 -*-

import sqlite3

conn = sqlite3.connect('hospitalData.sqlite')

cur = conn.cursor()

def dumpData(conn, cur):

    ziniarastis = cur.execute('SELECT paslaugos.pasl_kodas, gydytojai.spaudo_nr || " " || gydytojai.pavarde, ziniarastis.kons_viso, ziniarastis.data FROM ziniarastis INNER JOIN gydytojai ON gydytojai.id = ziniarastis.specialistas INNER JOIN paslaugos ON paslaugos.id = ziniarastis.paslauga')

    fhand = open('jsonData.js', 'w')

    for row in ziniarastis:
        print(row)

dumpData(conn, cur)
