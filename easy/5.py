from os import system

from  import abstractmethod, ABC

from colorama import Fore, Style

system('clear')

class Transport(ABC):



    @abstractmethod
    def move(self):
        pass
      
class Poyezd(Transport):
    def init(self):
        pass
    
    def move(self):
        return f"{Fore.BLUE}{Style.BRIGHT}\nPoyezd faqat relsda haqarakat qiladi"
    
class Avtobus(Transport):
    def init(self):
        pass      
      
    def move(self):
        return f"{Fore.BLUE}{Style.BRIGHT}\nAvtobus poyezdga qaraganda sekinroq yuradi"
    
def transports(transport):
    if transport == "Avtobus":
        return Avtobus()
    elif transport == "Poyezd":
        return Poyezd()
    else:
        print(f"{Fore.BLUE}{Style.BRIGHT}\nTransport topilmadi")
        return None
    
transport = transports("Avtobus")
print(transport.move())