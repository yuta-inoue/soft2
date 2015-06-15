class Student:
    name = None
    grade = None
    def __init__(self,name):
        self.name = name
        self.grade = 0
    def set_grade(self,grade):
        self.grade = grade
    def get_grade(self):
        return self.grade
    def get_name(self):
        return self.name
    def promotion(self):
        self.grade += 1
    def print_info(self):
        print("student name is %s (%d)"%(self.name,self.grade))
def main():
    s1 = Student("yamada")
    s2 = Student("suzuki")

    s1.set_grade(1)
    s2.set_grade(2)

    s1.print_info()
    s2.print_info()
    s1.promotion()
    s2.promotion()
    s1.print_info()
    s2.print_info()
if __name__ == "__main__":
    main()
