from os import system

from colorama import Fore, Style

system('clear')

class Animals:



    def init(self, type, age):
        self.type = type
        self.age = age
    
    def str(self):
        return (f"{Style.BRIGHT}{Fore.BLUE}{self.type} Yoshi: {Fore.YELLOW}{self.age}")
class predator(Animals):
    def init(self, type, age, food):
        super().init(type, age)
        self.food = food
    def voice(self):
        return (f"{Style.BRIGHT}{Fore.BLUE}{self.type} {Fore.YELLOW}ovoz chiqaradi!")
    def eat(self):
        return (f"{Style.BRIGHT}{Fore.BLUE}{self.type} {Fore.YELLOW}{self.food} yeydi")
class Herbivor(Animals):
    def init(self, type, age, ozuqa):
        super().init(type, age)
        self.ozuqa = ozuqa
    def voice(self):
        return (f"{Style.BRIGHT}{Fore.BLUE}{self.type} {Fore.YELLOW}ovoz chiqaradi")
    def eat(self):
        return (f"{Style.BRIGHT}{Fore.BLUE}{self.type} {Fore.YELLOW}{self.ozuqa} yeydi")
animar_prd = predator("Sher", 5, "Go'sht")

print(animar_prd)
print(animar_prd.voice())
print(animar_prd.eat())
animal_hrb = Herbivor("Qo'y", 3, "o't")
print(animal_hrb)
print(animal_hrb.voice())
print(animal_hrb.eat())