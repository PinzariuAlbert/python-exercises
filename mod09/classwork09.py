"""class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

dog = Dog("Bubbles", "Shefferd")

print(f"Name: {dog.name:s} breed: {dog.breed:s}." )"""

class Dog:
    created=0
    def __init__(self, name, birth_year, sound="woof woof"):
        self.name = name
        self.birth_year = birth_year
        self.sound=sound
        Dog.created+=1
    def bark(self, times):
        for i in range(times):
            print(self.sound)
        return
dog1 = Dog("Bubbles", 2022)
dog2=Dog("Ham", 2019, "yip yap")
print(f"{dog1.name:s} was born in {dog1.birth_year:d}." )
dog1.bark(1)
print(f"{dog2.name:s} was born in {dog2.birth_year:d}." )
dog2.bark(2)
print(f"Dog was used {Dog.created} times")