
def addService(conn, cur, pasl_kodas, pasl_pav):
    cur.execute('INSERT INTO paslaugos (pasl_kodas, pasl_pavadinimas) VALUES (?, ?)', (pasl_kodas, pasl_pav))

    print('Inserted in paslaugos table ' + pasl_kodas + ' '+ pasl_pav)

    conn.commit()
    return cur.execute('SELECT id FROM paslaugos WHERE pasl_kodas = ?', (pasl_kodas,)).fetchone()

def addSpecialist(conn, cur, sign, surname):
    cur.execute('INSERT INTO gydytojai (spaudo_nr, pavarde) VALUES (?, ?)', (sign, surname))

    print('Inserted in gydytojai table ' + sign + ' '+ surname)

    conn.commit()

    return cur.execute('SELECT id FROM gydytojai WHERE spaudo_nr = ?', (sign,)).fetchone()
