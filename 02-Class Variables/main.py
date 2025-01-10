# Class variables: Shared among all instances of a class
#                  Defined outside the constucter
#                  Allow you to share data among all objects created from that class

class Student:

    class_year = 2024 # Class Variable
    num_students = 0 # Class Variable

    def __init__(self, name, age):
        self.name = name
        self.age = age
        Student.num_students += 1 # self는 student1, student2를 의미하므로
                                  # class variable을 modify 할 때는 클래스 이름(Student)를 사용함


student1 = Student("Spongebob", 30)
student2 = Student("Patrick", 35)
student3 = Student("Sqidward", 55)
student4 = Student("Sandy", 27)

print(student2.name) # Patrick
print(student2.age) # 35
print(Student.class_year) # 2024
                          # 클래스 자체로 access 하는 것이 명확한 표현임 (인스턴스로 호출x, e.g. student1.class_year x)

print(Student.num_students) # 4

print(f"My graduating class of {Student.class_year} has {Student.num_students} students") # My graduating class of 2024 has 4 students
