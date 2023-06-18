from colorama import Fore
from Functions import AddPatient
from Functions import FindPatient

class Routers(object):
    def Router():
        name = input("\n Hastanın Adı: ")
        surname = input("\n Hastanın Soyadı: ")
            
        if name == "" or surname == "":
            print(Fore.LIGHTBLUE_EX + "\n Lütfen Hasta Adı Soy Adı Belirtiniz!")
            
        TC_NO_Data = input("\n Hastanın Kimlik Numarası: ")
        if TC_NO_Data == "":
            print(Fore.LIGHTBLUE_EX + "\n Hastanın Kimlik Numarası Boş Bırakılamaz")
                
        disease_illness = input("\n Şikayet: Hastalık/Belirti: ")
        if disease_illness == "":
            print(Fore.LIGHTBLUE_EX + "\n Hastalık Adı Boş Bırakılamaz")

        blood_group = input("\n Hastanın Kan Grubu: ")
        if disease_illness == "":
            print(Fore.LIGHTBLUE_EX + "\n Hastalık Adı Boş Bırakılamaz")
                
        age = input("\n Hastanın Yaşınız: ")
        if age == "":
            print(Fore.LIGHTBLUE_EX + "\n Yaş Boş Bırakılamaz")
                
        kilo = input("\n Hastanın Kilonuz: ")
        if kilo == "":
            print(Fore.LIGHTBLUE_EX + "\n Kilo Boş Bırakılamaz")
                
        size = input("\n Hastanın Boyu: ")
        if size == "":
            print(Fore.LIGHTBLUE_EX + "\n Boy Boş Bırakılamaz")
                
        mothers_name = input("\n Hastanın Annesinin Adı: ")
        if mothers_name == "":
            print(Fore.LIGHTBLUE_EX + "\n Hastanın Annesinin Adı Boş Bırakılamaz")
                
        fathers_name = input("\n Hastanın Babasının Adı: ")
        if fathers_name == "":
            print(Fore.LIGHTBLUE_EX + "\n Hastanın Babasının Adı Boş Bırakılamaz")
                
        allergic_diseases = input("\n Hastanın Alerjik Hastalıkları: ")
        if allergic_diseases == "":
            print(Fore.LIGHTBLUE_EX + "\n Hastanın Alerjik Hastalıkları Boş Bırakılamaz")
                
        covid_vaccine_status = input("\n Hastanın COVID-19 Aşı Durumu: ")
        if covid_vaccine_status == "":
            print(Fore.LIGHTBLUE_EX + "\n Hastanın COVID-19 Aşı Durumu Boş Bırakılamaz")
        

        AddPatient.Add(name,surname,disease_illness,blood_group,age,kilo,size,mothers_name,fathers_name,allergic_diseases,covid_vaccine_status,TC_NO_Data)
        
    def FindRouter():
        name = input("\n Hastanın Adı: ")
        surname = input("\n Hastanın Soyadı: ")
        
        # İstersen buraya tc no ekleme sistemini getirisin ben add kısmına kodlarım burasi sana kalmis
            
        if name == "" or surname == "":
            print(Fore.LIGHTBLUE_EX + "\n Lütfen Hasta Adı Soy Adı Belirtiniz!")
        
        FindPatient.Find(name,surname)    