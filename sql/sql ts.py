import mysql.connector



yhteys = mysql.connector.connect(
         host='127.0.0.1',
         port= 3306,
         database='flight_game',
         user='bob',
         password='dingle',
         autocommit=True
         )

def hae_suomen_lentokentat():
    sql = "SELECT name FROM airport WHERE iso_country='FI'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    for rivi in tulos:
        print(rivi[0])  # rivi[0] on kentän nimi
    return


hae_suomen_lentokentat()
