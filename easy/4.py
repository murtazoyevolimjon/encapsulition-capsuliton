from os import system

from colorama import Fore

system('clear')

class Car:


    
    def init(self, car=None, price=None, marka=None) -> None:
        self.car = car
        self.price = price
        self.age = marka
        
    def getter(self):
        self.car = input(f"{Fore.YELLOW}\nname:{Fore.BLUE} ")
        self.marka = input(f"{Fore.YELLOW}marka:{Fore.BLUE} ")
        self.price = int(input(f"{Fore.YELLOW}price:{Fore.BLUE} "))
        
    def setter(self):
        print(f"{Fore.YELLOW}\nName: {Fore.BLUE}{self.car}{Fore.YELLOW}\nMarka: {Fore.BLUE}{self.marka}\n{Fore.YELLOW}Price: {Fore.BLUE}{self.price}")
    def price_change(self, car_name):
        count = 0
        self.car = car_name
        for car in cars:
            if car.car.upper() == car_name.upper():
                car.price = input(f"{Fore.YELLOW}Yangi narxni kiriting:{Fore.BLUE} ") 
                print(f"\n{Fore.YELLOW}Mashina narxi o'zgartirildi")
                count+= 1
    
    
cars =  []
n = 0  
while True:
    print(f"\n{Fore.YELLOW}Mashina qo'shish - {Fore.BLUE}1\n{Fore.YELLOW}Barcha kiritilgan mashinalarni ko'rish - {Fore.BLUE}2\n{Fore.YELLOW}Mashina narxini o'zgartirish - {Fore.BLUE}3\n{Fore.YELLOW}Dasturdan chiqish - {Fore.BLUE}4")
    
    n = int(input(f"{Fore.YELLOW}Buyruq tanlang:{Fore.BLUE} "))
    
    car = Car()
    if n == 1:
        car.getter()
        cars.append(car) 
        
    if n == 2:
        for car in cars:
            car.setter()
                
    if n == 3:
        s1 = input(f"\n{Fore.YELLOW}qaysi mashina narxini o'zgartirmoqchisiz:{Fore.BLUE} ")
        car_name = Car()
        car_name.price_change(s1)
    
    if n== 4:
        break
    
    if n <= 0 or n > 4:
        print(f"\n{Fore.YELLOW}Bunday buyruq mavjud emas")