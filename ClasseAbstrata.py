from abc import ABC, abstractmethod

class  Animal(ABC):
    @abstractmethod
    def fazer_som(self):
        pass

class Cachorro(Animal):
    def fazer_som(self):
        return "Au Au!"
    
class Gato(Animal):
    def fazer_som(self):
        return "Miau!"
    
animal = Cachorro()
print(animal.fazer_som())
animal = Gato()
print(animal.fazer_som())