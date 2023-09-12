"""class Employee:
    def __init__(self,name,id__):
        self.name=name
        self.id__=id__
    def display(self):
        print("NAME:%s\nID:%s"%(self.name,self.id__))
    def compare(self,other):
        if self.id__==other.id__:
            return True
        else:
            return False
emp1=Employee("Jhon","2115A022")
emp2=Employee("Paul","2115A022")
emp1.name="Mahesh"
emp1.display()
emp2.display()
print(emp1.id__)
if emp1.compare(emp2):
    print("They are same")
else:
    print("They are different")"""
class student:
    count=0   #class or static variable
    def __init__(self):
        student.count=student.count+1
s1=student()
s2=student()
s3=student()
s4=student()
s5=student()
print("no.of students=%d"%student.count)
