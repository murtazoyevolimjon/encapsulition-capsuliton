class Taxi:
    
    def init(self, name=None, car=None, price=None, path= None, space= None) -> None:
        self.name = name
        self.car = car
        self.__price = price
        self.__path= path
        self.__space = space
        
    def getter(self):
        self.__price = int(input("\nNarxni kiriting: "))
        
    def setter(self):
        space = int(input("Bo'sh joy  qo'shish: "))
        if space > 0:
            self.__space = space
        else:
            print(f"Joy 0 dan katta bo'lishi kerak")
            
    def change(self):
        self.name = input("Yangi haydovchi ismini kiriting: ")
        self.car = input("Mashina turini kriting: ")
        
    
    def show_info(self):
        print(f"\nHaydovchi: {self.name}, Mashina:{self.car}, Narx:{self.__price}$, Yo'nalish:{self.__path}, Bo'sh joy:{self.__space}")
    
taxi1 = Taxi("Nurbek Abdullayev", "Nexia 2", 10, "Shahar Markazi", 3)
taxi2 = Taxi("Sherbek Nizomiddinov", "Tesla", 15, "Shahar burchagi", 2)
taxis = [taxi1, taxi2]
for Taxi in taxis:
    Taxi.show_info()
for Taxi in taxis:
    Taxi.getter()
    Taxi.setter()
    Taxi.change()
print("\nMalumotlar yangilandi:")
for Taxi in taxis:
    Taxi.show_info()