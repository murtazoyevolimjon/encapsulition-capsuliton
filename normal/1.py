class Car:


    def init(self, model, color, price, brand, manufacture_year):
        self.model = model  
        self.color = color  
        self.price = price  
        self.__brand = brand  
        self.__manufacture_year = manufacture_year  

    def get_price(self):
        return self.__price
    def get_manufacture_year(self):
        return self.__manufacture_year
    def set_price(self, new_price):
        if new_price < 0:
            
            print("Price cannot be negative!")
        else:
            self.__price = new_price
if __name__ == "__main__":
    cars2 = Car("Malibu", "White", 35000, "Chevrolet", 2024) 
    print(f"Model: {cars2.model}")
    print(f"Color: {cars2.color}")
    new_color = input("Enter new color: ")
    cars2.color = new_color
    print(f"Updated Color: {cars2.color}")
    print(f"Price: {cars2.get_price()} $")
    print(f"Manufacture Year: {cars2.get_manufacture_year()}")
    new_price = int(input("Enter new price: "))
    cars2.set_price(new_price)
    print(f"Updated Price: {cars2.get_price()} $")