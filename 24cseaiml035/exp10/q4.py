class parent():
    def show (self):
        print("parent class")
class child (parent):
    def show (self):
        print("child class ")
s=child()
s.show()
y=parent()
y.show()