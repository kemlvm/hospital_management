import os
import time
import math
from Interface import UserInterface
import mysql.connector
from colorama import Fore
from Functions import AddPatient
from Utils import Routers
from MysqlConnector import connector

class TextValues(object):
    InputTextHello = "Program Arayüzü Başarılı Bir Şekilde Aktifleştirildi! \n"
    WelcomeSystem = "Hastane/Hasta Yönetim Sistemine Hoşgeldiniz!"
    LoginText = "Aşağıdan Kullanıcı Adınızı ve Şifrenizi Girerek Sisteme Erişim Sağlayabilirsiniz!"
    SuccesfulyLogin = "Başarılı Giriş"
    Error = "Hatalı kullanıcı adı veya şifre!"


UserInterface.LocalObject.Start(TextValues.InputTextHello,TextValues.WelcomeSystem,TextValues.LoginText)

LoginMainOne = str(input("\n Kullanıcı Adınızı Giriniz: ")) #TODO Kullanıcı Adınızı Giriniz!
LoginMainTwo = input("\n Şifrenizi Giriniz: ") #TODO Şifrenizi Giriniz!

# Veritabanından kullanıcıyı sorgula
cursor = connector.MyMysqlSettings.MyDatabaseSettings.cursor()
query = "SELECT * FROM administrator_table WHERE username = %s AND password = %s"
cursor.execute(query, (LoginMainOne, LoginMainTwo))
MainInterface = cursor.fetchone()

if MainInterface:
    print(Fore.LIGHTBLUE_EX + f"\n {TextValues.SuccesfulyLogin}")
    time.sleep(2)
    
    os.system("cls")
    
    print(Fore.BLUE + f"\n {UserInterface.LocalObject.Choose}")
    
    GET_DATA = input("\n Yapacağınız İşlemi Seçin: ")
    
    if (GET_DATA == "1"):
        os.system("cls")
        Routers.Routers.Router() #TODO Yönlendiriciden Çektik!
    elif (GET_DATA == "2"):
        Routers.Routers.FindRouter()
        
    elif (GET_DATA == "3"):
        exit()
        
else:
    print(Fore.RED + f"\n {TextValues.Error}") 