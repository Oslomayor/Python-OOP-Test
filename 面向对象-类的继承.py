# 11:07 PM, Feb 9th, @ dormitory
# 面向对象，类的继承
# 继承 inherit
# 类的继承基本理解，还要多写代码练习加深印象

class SchoolMember:
    
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Initilized SchoolMember: {0})'.format(self.name))

    def tell(self):
        print('Name:{0} Age:{1}'.format(self.name, self.age))
        
# Teacher 类继承 SchoolMember 类
class Teacher(SchoolMember):
    # 初始化函数
    def __init__(self, name, age, salary):
        # 调用父类 SchoolMember 的初始化函数
        SchoolMember.__init__(self, name, age)
        # 补充子类的属性
        self.salary = salary
        print('(Initilized Teacher: {0})'.format(self.name))

    def tell(self):
        # 调用父类 SchoolMember 的方法
        SchoolMember.tell(self)
        print('Salary: {0}'.format(self.salary))

# Student 类继承 SchoolMember 类
class Student(SchoolMember):
    
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('(Initlized Student: {0})'.format(self.name))

    def tell(self):
        SchoolMember.tell(self)
        print('Marks: {0}'.format(self.marks))

pass
# Flora = SchoolMember('Flora', 25)
# Denis = SchoolMember('Denis', 23)
# Flora = Teacher('Flora', 29, 8000)
# Denis = Student('Denis', 23, 99)
        

