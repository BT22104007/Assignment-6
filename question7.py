class Student:
    pass

class Marks:
    pass

akshit=Student()

akshit_marks=Marks()

print("sambhav is an instance of class Student:",isinstance(akshit,Student))
print("sambhav is an instance of class Marks:",isinstance(akshit,Marks))
print("sambhav_ke_marks is an instance of class Student:",isinstance(akshit_marks,Student))
print("sambhav_ke_marks is an instance of class Marks:",isinstance(akshit_marks,Marks))

print("Student is a subclass of class object:",issubclass(Student,object))
print("Marks is a subclass of class object:",issubclass(Marks,object))