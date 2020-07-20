# -*- coding: utf-8 -*-
if __name__ == '__main__':
    import sqlite3

    conn = sqlite3.connect('hospitalData.sqlite')

    cur = conn.cursor()

    ziniarastis = cur.execute('SELECT paslaugos.pasl_kodas, gydytojai.spaudo_nr || " " || gydytojai.pavarde, ziniarastis.kons_viso, ziniarastis.data FROM ziniarastis INNER JOIN gydytojai ON gydytojai.id = ziniarastis.specialistas INNER JOIN paslaugos ON paslaugos.id = ziniarastis.paslauga').fetchall()

    fhand = open('jsonData.js', 'w')
    fhand.write("let allData = [")

    for i in range(len(ziniarastis)):
        # fhand.write("{")
        # fhand.write("serviceCode:" + str(ziniarastis[i][0]) + ",")
        # fhand.write("doctor:" + " ".join(str(ziniarastis[i][1]).split(" ")) + ",")
        # fhand.write("serviceCount:" + str(ziniarastis[i][2]) + ",")
        # fhand.write("serviceTime:" + str(ziniarastis[i][3]))
        # if i < len(ziniarastis) - 1:
        #     fhand.write("},")
        # else:
        #     fhand.write("}")
        fhand.write("[")
        fhand.write('"' + str(ziniarastis[i][0]) + '",')
        fhand.write('"' + str(ziniarastis[i][1]) + '",')
        fhand.write('"' +str(ziniarastis[i][2]) + '",')
        fhand.write('"' + str(ziniarastis[i][3]) + '"')
        if i < len(ziniarastis) - 1:
            fhand.write("],")
        else:
            fhand.write("]")
    fhand.write("]")
