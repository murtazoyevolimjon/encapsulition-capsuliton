class Animal:

    def init(self, species, weight):
        self.species = species  
        self.weight = weight 

class Dog(Animal):

    def make_sound(self):
        return "vov-vov"
    
class Cat(Animal):
    
    def make_sound(self):
        return "miyov-miyov"
    
class Bookstore:
    def init(self, name, location, books, services):

        self.name = name
        self.location = location 
        self.books = books  
        self.services = services 

    def scientific_books(self):

        for book in self.books:
            if "ilmiy" in book.lower():
                return True
        return False
    
if __name__ == "__main__":
    bookstore1 = Bookstore(
        "Kitoblar", 
        "Toshkent", 
        ["Ilmiy Fizika", "Tarix", "Kimyo", "Matematika"], 
        ["Yetkazib berish"]
    )
    bookstore2 = Bookstore(
        "Badiy Kitoblar", 
        "Samarqand", 
        ["Roman", "Bolalar kitoblari"], 
        ["Xizmatlar mavjud emaas"]
    )
    bookstore3 = Bookstore(
        "Adabiy kitoblar", 
        "Samarqand", 
        ["Ilmiy Biologiya" ], 
        ["Yetkazib berish"]
    )
    bookstores = [bookstore1, bookstore2, bookstore3]
    print("Ilmiy kitoblar mavjud bo'lgan do'konlar:")
    for store in bookstores:
        if store.scientific_books():
            print(f"Do'kon nomi: {store.name}, Joylashuvi: {store.location}, Xizmatlar: {', '.join(store.services)}")
 
    dog = Dog("It", 15)
    cat = ("Mushuk", 5)
    while True:
        print("\nQaysi hayvonning ovozini eshitmoqchisiz?", 
              "\n1. It", 
              "\n2. Mushuk", 
              "\n3. Chiqish")
        chooce = input("Quyidagi menyulardan birini tanlang: ")
        if chooce == "1":
            print(f"{dog.species}: {dog.make_sound()}")
        elif chooce == "2":
            print(f"{cat.species}: {cat.make_sound()}")
        elif chooce == "3":
            print("Exiting...")
            break
        else:
            print("Notogri tanlov, qaytadan urinib ko'ring")