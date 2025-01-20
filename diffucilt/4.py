class Mashina:
    
    def init(self, name=None, color=None, price=None, speed=None, fuel_type=None) -> None:

        self.name = name
        self.color = color
        self.__speed = speed
        self.__price = price
        self.__fuel_type = fuel_type
        
    def getter(self):
        print(f"Tezlik: {self.__speed} km/h")
        
    def setter(self):
        gas_type = input("Yangi yoqilg'i turi: ")
        self.__fuel_type = gas_type
        print(f"Yoqilg'i turi yangilandi: {self.__fuel_type}")
            
    def change(self):
        self.name = input("Yangi mashina nomini kiriting: ")
        self.color = input("Yangi mmashina rangini kiriting: ")
        
    def show_info(self):
        print(f"\nMashina nomi: {self.name}, Rangi: {self.color}, Narxi: {self.__price}$, Tezligi: {self.__speed} km/h, Yoqilg'i turi: {self.__fuel_type}")
mashina1 = Mashina("Gentra", "Qora", 14000, 100, "Gaz")
mashina2 = Mashina("BMW", "Qora", 50000, 140, "Electr")
mashina3 = Mashina("Tesla", "Oq", 21000, 80, "Electr")
cars = [mashina1, mashina2, mashina3]
for car in cars:
    car.show_info()
for car in cars:
    car.getter()
    car.setter()
    car.change()
print("\nMalumot yangilandi:")
for car in cars:
    car.show_info()