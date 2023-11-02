import student as st
class Controler():
    def __init__(self):
        self.__students={}

    def addStudent(self,dni,name,surname,age,city,province,email):
        if dni not in self.__students:
            student=st.Student(dni,name,surname,age,city,province,email)
            self.__students[dni]=student
            return True
        return False
    
    def delStudent(self,dni):
        if dni in self.__students:
            student=self.__students.pop(dni)
            return student
        return None
    
    def modStudent(self,student,option,newValue):
        if option == "1":
            student.set_age(newValue)
            return student
        elif option == "2":
            student.set_city(newValue)
            return student
        elif option == "3":
            student.set_province(newValue)
            return student
        elif option == "4":
            student.set_email(newValue)
            return student
        
    def search_student(self,dni):
        if dni in self.__students:
            student = self.__students[dni]
            return student
        else:
            return None


