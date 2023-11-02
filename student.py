class Student:
    def __init__(self,dni,name,surnames,age,city,province,email):
        self.__dni=dni
        self.__name=name
        self.__surnames=surnames
        self.__age=age
        self.__city=city
        self.__province=province
        self.__email=email

# Getter and setter 
    #dni
    def get_dni(self):
        return self.__dni
    #name
    def get_name(self):
        return self.__name
    #surname
    def get_surnames(self):
        return self.__surnames
    #age
    def get_age(self):
        return self.__age
    def set_age(self, age):
        self.__age = age
    #city
    def get_city(self):
        return self.__city
    def set_city(self, city):
        self.__city = city
    #province
    def get_province(self):
        return self.__province
    def set_province(self, province):
        self.__province = province
    #Email
    def get_email(self):
        return self.__email
    def set_email(self, email):
        self.__email = email

    
        
