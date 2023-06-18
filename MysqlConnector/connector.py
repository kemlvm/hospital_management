import mysql.connector


class MyMysqlSettings(object):
    MyDatabaseSettings = mysql.connector.connect(
        host="localhost",
        user="root", # genellikle root olur
        password="",  # MySQL parolanı buraya gir (GENELLİKLE PASSWORD BOS KALIR YOKTUR PASSWORD BOYLE KALSIN)
        database="hospital_administrator"  # Veritabanı adını buraya gir
    )