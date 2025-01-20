from os import system

from colorama import Fore, Style

system('clear')

class Telefon:



    def init(self, name=None, number=None) -> None:
        self._name = name
        self._number = number
    
    def enter(self):
        self._name = input("\nIsmni kiriting-> ")
        self._number = input("Telefon raqamni kiriting-> ")
        
    def out(self):
        print (f"{Fore.GREEN}\nIsm-> {Fore.RED}{self._name}\n{Fore.GREEN}Telefon raqam-> {Fore.RED}{self._number}")
phones =  []
n = 0  
while True:
    print(f"\n{Fore.BLUE}{Style.BRIGHT}Kontakt qo'shish - 1", "Kontaktlar ro'yxati - 2", "Dasturni to'xtatish - 7", sep='\n')
    
    n = int(input("Buyruqni tanlang: "))
    phone = Telefon()
    if n == 1:
        phone.enter()
        phones.append(phone)
        
    if n == 2:
        for phone in phones:
            phone.out()
    
    if n == 0:
        break
    
    if n > 7 or n <= 0:
        print(f"{Fore.BLUE}\nBunday buyruq yuq")