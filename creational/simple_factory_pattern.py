from abc import ABC, abstractmethod
from enum import Enum


'''an enumeration for animal types'''
class AnimalType(Enum):
    DOG = "Dog"
    CAT = "Cat"
    FISH = "Fish"


'''an abstract Animal class'''
class Animal(ABC):
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age

    @abstractmethod
    def get_info(self) -> str:
        pass


'''concrete animal classes'''
class Dog(Animal):
    def get_info(self) -> str:
        return f"Dog - Name: {self.name}, Age: {self.age}"


class Cat(Animal):
    def get_info(self) -> str:
        return f"Cat - Name: {self.name}, Age: {self.age}"


class Fish(Animal):
    def get_info(self) -> str:
        return f"Fish - Name: {self.name}, Age: {self.age}"


'''an AnimalFactory class'''
class AnimalFactory:
    def create_animal(self, animal_type: AnimalType, context: dict) -> Animal:
        # Implement the logic to create an animal based on the animal_type parameter and context data
        if animal_type == AnimalType.DOG:
            return Dog(context["name"], context["age"])
        elif animal_type == AnimalType.CAT:
            return Cat(context["name"], context["age"])
        elif animal_type == AnimalType.FISH:
            return Fish(context["name"], context["age"])
        else:
            raise ValueError(f"Invalid animal type: {animal_type}")


def main():
    animal_factory = AnimalFactory()

    # Test the AnimalFactory by creating different types of animals and passing context data
    dog = animal_factory.create_animal(AnimalType.DOG, {"name": "Buddy", "age": 3})
    print(dog.get_info())

    cat = animal_factory.create_animal(AnimalType.CAT, {"name": "Whiskers", "age": 2})
    print(cat.get_info())

    fish = animal_factory.create_animal(AnimalType.FISH, {"name": "Goldie", "age": 1})
    print(fish.get_info())


if __name__ == "__main__":
    main()
