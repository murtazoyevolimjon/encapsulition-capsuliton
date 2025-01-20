from os import system

from colorama import Fore, Style

system('clear')

class Xodim:


    def init(self, name, age, rank):
        self._name = name
        self._age = age
        self._rank = rank
    def get_name(self):
        return self._name
    def set_name(self, new_name):
        self._name = new_name
    def get_age(self):
        return self._age
    def set_age(self, new_age):
        self._age = new_age
            
    def get_rank(self):
        return self._rank
    def set_rank(self, new_rank):
        self._rank = new_rank
        
employee = Xodim("Aliye Vali", 21, "Sotuvchi")

print(f"{Style.BRIGHT}{Fore.BLUE}Ism familiya-> {Fore.RED}{employee.get_name()}")
print(f"{Fore.BLUE}Yosh-> {Fore.RED}{employee.get_age()}")
print(f"{Fore.BLUE}Lavozim-> {Fore.RED}{employee.get_rank()}")
employee.set_rank("Katta sotuvchi")
print(f"{Fore.GREEN}Yangi lavozimi-> {Fore.RED}{employee.get_rank()}")