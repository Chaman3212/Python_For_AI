class student:
    def __init__(self,name,cgpa):
        self.name= name
        self.cgpa = cgpa
    def get_cgpa(self):
        return self.cgpa


stu1= student("Rahul",9.2)
stu2= student("Rajiv",7.6)
stu3= student("Rakesh",8.9)

print(f"the name of the student is {stu1.name} and the cgpa is {stu1.cgpa}")
