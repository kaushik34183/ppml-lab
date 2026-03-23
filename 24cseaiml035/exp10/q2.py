
class GrandParent:
    def property(self):
        print("GrandParent: Owns a large property")
class Parent(GrandParent):
    def business(self):
        print("Parent: Runs a business")
class Child(Parent):
    def education(self):
        print("Child: Studying in college")
if __name__ == "__main__":
    child = Child()
    print("=== Multilevel Inheritance Demo ===")
    print()
    child.property()    
    child.business()    
    child.education() 
    print()
    print("=== Demonstrating that Child has access to all methods ===")
    print("Child can access:")  
    print("- property() method from GrandParent class")
    print("- business() method from Parent class")
    print("- education() method from Child class")
