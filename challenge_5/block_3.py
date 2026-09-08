from abc import abstractmethod, ABC

class Vehicule(ABC):
    def __init__(self, marque='', immatriculation=''):
        self.marque = marque
        self.__immatriculation = immatriculation

    @property
    def immatriculation():
        return self.__immatriculation

    @abstractmethod
    def daily_price(self, base_price):
        pass

class Voiture(Vehicule):
    def __init__(self, places_number=5, marque='', immatriculation=''):
        super().__init__(marque, immatriculation)
        try:
            self.places_number = int(places_number)
        except ValueError:
            self.places_number = 5
            print('[!] Le nombre entré est invalide, le nombre actual est 5 place et vous pouvez le changer.')

    def daily_price(self, base_price):
        return base_price + self.places_number

    def __str__(self):
        print(f'[+] Voiture {self.marque} -> ({self.__immatriculation}) -- {self.places_number} places -- {self.daily_price(40)}/jour')

class Moto(Vehicule):
    def __init__(self, cylinders=6, marque='', immatriculation=''):
        super().__init__(marque, immatriculation)
        try:
            self.cylinders = int(cylinders)
        except ValueError:
            self.cylinders = 6
            print('[!] Le nombre entré est invalide, le nombre actual est 6 cylinders et vous pouvez le changer.')

    def daily_price(self, base_price):
        return base_price + self.cylinders

    def __str__(self):
        print(f'[+] Moto {self.marque} -> ({self.__immatriculation}) -- {self.cylinders} cylindree -- {self.daily_price(40)}/jour')
        
class Camion(Vehicule):
    def __init__(self, kg_weights=100, marque='', immatriculation=''):
        super().__init__(marque, immatriculation)
        try:
            self.kg_weights = int(kg_weights)
        except ValueError:
            self.kg_weights = 100
            print('[!] Le nombre entré est invalide, le nombre actual est 100 KG et vous pouvez le changer.')

    def daily_price(self, base_price):
        return base_price + self.kg_weights

    def __str__(self):
        print(f'[+] Camion {self.marque} -> ({self.__immatriculation}) -- {self.kg_weights} KG -- {self.daily_price(40)}/jour')