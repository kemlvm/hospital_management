import os
from colorama import Fore

class LocalObject(object):
    """

    Args:
        object (_type_): _description_
    """
    
    Choose = """
    
    1- Hasta Kaydet [1]
    2- Hasta Bul    [2]
    3- Çıkış Yap    [3]
    
    """
    
    def Start(Text1,Text2,Text3):
    
        os.system("cls")
        
        print(Fore.RED + f"{Text1}")
        print(Fore.LIGHTMAGENTA_EX + f"{Text2}")    
        print(Fore.LIGHTMAGENTA_EX + f"{Text3}")