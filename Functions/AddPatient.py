import mysql.connector
from colorama import Fore

MysqlDatabase = mysql.connector.connect(
    host="localhost",
    user="root", # genellikle root olur
    password="",  # MySQL parolanı buraya gir (GENELLİKLE PASSWORD BOS KALIR YOKTUR PASSWORD BOYLE KALSIN)
    database="hospital_administrator"  # Veritabanı adını buraya gir
)

def Add(Name,Surname,Disease_illness,Blood_group,Age,Kilo,Size,Mothers_name,Fathers_name,Allergic_diseases,Covid_vaccine_status,TC_NO):
    cursor = MysqlDatabase.cursor()
    query = "INSERT INTO patients (name, surname, disease_illness, blood_group, age, kilo, size, mothers_name, fathers_name, allergic_diseases, covid_vaccine_status,tc_no) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    values = (Name, Surname, Disease_illness, Blood_group, Age, Kilo, Size, Mothers_name, Fathers_name, Allergic_diseases, Covid_vaccine_status, TC_NO)
    cursor.execute(query, values)
    MysqlDatabase.commit()
    print(Fore.LIGHTBLUE_EX + "\n Hasta Verileri Başarılı Bir Şekilde Sisteme Girildi!")
