class father:
    def skill1(self):
        print("skill 1")
class mother:
    def skill2(self):
        print("skill2")
class child(father,mother):
    def skill3(self):
        print("skill3")
obj=child()
obj.skill1()
obj.skill2()
obj.skill3()
