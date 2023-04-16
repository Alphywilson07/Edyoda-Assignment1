# 👉 1. Create a class named ‘Dog’. It should have a constructor which accepts its name, age and coat color. You must perform the following operations:

# 🔴 a. It should have a function ‘description()’ which prints the name and age of the dog.
# 🔴 b. It should have a function ‘get_info()’ which prints the coat color of the dog.
# 🔴 c. Create child classes ‘JackRussellTerrier’ and ‘Bulldog’ which is inherited from the class ‘Dog’. It should have at least two methods of its own.
# 🔴 d. Create objects and implement the above functionalities.
class Dog:
    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    def description(self):
        print(f"{self.name} is {self.age} years old.")

    def get_info(self):
        print(f"{self.name} has {self.coat_color} coat color.")


class JackRussellTerrier(Dog):
    def __init__(self, name, age, coat_color):
        super().__init__(name, age, coat_color)

    def bark(self):
        print(f"{self.name} is barking.")


class Bulldog(Dog):
    def __init__(self, name, age, coat_color):
        super().__init__(name, age, coat_color)

    def run(self):
        print(f"{self.name} is running.")


# Create Dog objects
dog1 = Dog("Rex", 3, "brown")
dog2 = Dog("Max", 5, "black")

# Test Dog methods
dog1.description()
dog2.get_info()

# Create JackRussellTerrier object
jrt = JackRussellTerrier("Jack", 2, "white")

# Test JackRussellTerrier methods
jrt.description()
jrt.get_info()
jrt.bark()

# Create Bulldog object
bulldog = Bulldog("Rocky", 4, "grey")

# Test Bulldog methods
bulldog.description()
bulldog.get_info()
bulldog.run()
