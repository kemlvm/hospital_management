import mysql.connector
from colorama import Fore

MysqlDatabase = mysql.connector.connect(
    host="localhost",
    user="root", # genellikle root olur
    password="",  # MySQL parolanı buraya gir (GENELLİKLE PASSWORD BOS KALIR YOKTUR PASSWORD BOYLE KALSIN)
    database="hospital_administrator"  # Veritabanı adını buraya gir
)

def Find(Name,Surname):
    cursor = MysqlDatabase.cursor()
    query = "SELECT * FROM patients WHERE name = %s AND surname = %s"
    values = (Name, Surname)
    cursor.execute(query, values)
    results = cursor.fetchall()

    if len(results) == 0:
        print(Fore.LIGHTYELLOW_EX + "\n Hasta bulunamadı!")

    else:
        print(Fore.LIGHTGREEN_EX + "\n Hasta Bilgileri:")
        for result in results:
            print("-------------------------------")
            print("\n Hastanın Adı: ", result[1])
            print("\n Hastanın Soyadı: ", result[2])
            print("\n Hastanın Hastalık/Belirti: ", result[3])
            print("\n Hastanın Kan Grubu: ", result[4])
            print("\n Hastanın Yaş: ", result[5])
            print("\n Hastanın Kilo: ", result[6])
            print("\n Hastanın Boy: ", result[7])
            print("\n Hastanın Annenin Adı: ", result[8])
            print("\n Hastanın Babanın Adı: ", result[9])
            print("\n Hastanın Alerjik Hastalıklar: ", result[10])
            print("\n Hastanın COVID-19 Aşı Durumu: ", result[11])
            print("-------------------------------")
