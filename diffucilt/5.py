class Laptop:
    
    def init(self, brand, price, battery_life) -> None:
        self.brand = brand
        self.price = price
        self.battery_life = battery_life
        
    def apply_discount(self):
        if self.battery_life < 5:
            discount = self.price * (10 / 100)
            self.price -= discount
    
    def check_battery(self):
        self.apply_discount()
    def show_info(self):
        if self.battery_life < 5:
            print(f"Brendi: {self.brand}, Narxi: {self.price}$, Batareya vaqti: {self.battery_life} soat. Batareyaning ishlash vaqti kam")
        else:
            print(f"Brendi: {self.brand}, Narxi: {self.price}$, Batareya vaqti: {self.battery_life} soat")
laptop1 = Laptop("Apple 16 Pro", 1200, 8)
laptop2 = Laptop("Samsung S23 ultra", 900, 10)
laptop3 = Laptop("Redmi 12", 200, 4)
laptop4 = Laptop("Poco X4 pro", 300, 10)
laptops = [laptop1, laptop2, laptop3, laptop4]
for laptop in laptops:
    laptop.check_battery()
    laptop.show_info()