
class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        """Method that will be inherited by child class"""
        print(f"{self.name} makes a sound")

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name) 
        self.breed = breed
    
if __name__ == "__main__":
    dog = Dog("Buddy", "Golden Retriever")
    print("Calling the inherited speak() method:")
    dog.speak()
    print(f"Dog's name: {dog.name}")
    print(f"Dog's breed: {dog.breed}")
