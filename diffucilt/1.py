class Robot:
    
    def init(self, model_num, area, charge, max_work, status) -> None:
        self.model_num = model_num
        self.area = area
        self.charge = charge
        self.max_work = max_work
        self.status = status
        
    def getter(self):
        print("\n")
        if int(self.charge) <= 20:
            print(f"\nModel number: {self.model_num}\nArea: {self.area}\nBattary {self.charge}%, Zaryadlash kerak\nMax ish vaqti: {self.max_work}\nStatus: {self.status}")
        else:
            print(f"\nModel number: {self.model_num}\nArea: {self.area}\nBattary is {self.charge}%, Battery is enough!\nMaximum working time: {self.max_work}\nStatus: {self.status}")
            
            
    def setter(self):
        model_number = input("Telefon nomini kiriting: ")
        for model in robots:
            if model_number == model.model_num:
                new_time =  int(input("Yangi ish vaqtini kiriting: "))
                if new_time <= 12:
                    model.max_work = new_time
                    print(f"Yangi ish vaqti qo'yildi")
                    break
                else:
                    print(f"Max ish vaqti 20 soat")
                    break
                
    
    def status(self):
        if self.status == "Kutmoqda":
            self.charge = 100
    
robot1 = Robot("Samsung S23", "Bloger", 15, 10, "Kutmoqda")
robot2 = Robot("iPhone 14", "Bloger", 45, 8, "Ishlayapdi")
robot3 = Robot("Redmi Note 12", "Bloger", 10, 12, "Kutmoqda")
robots = [robot1, robot2, robot3]
n = 0
while True:
    print("\nMavjud telefonlarni ko'rish - 1: ", 
          "Ishlash vaqtini o'zgartirish - 2: ",
          "Dasturni to'xtatish - 3", sep="\n")
    n = int(input("Buyruqni tanlang: "))
    
    if n == 1:
        for robot in robots:
            robot.getter()
            
    if n == 2:
        for robot in robots:
            robot.setter()
    
    if n == 3:
        break
    
    if n <= 0 or n > 3:
        print("\nBunday buyruq mavjud emas")