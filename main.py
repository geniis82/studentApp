import controler as sc
controllerStudent=sc.Controler()

def controlDni(dni):
        letraDni="TRWAGMYFPDXBNJZSQVHLCKE"
        numDni=int(dni[:-1])
        letraCal=letraDni[numDni % 23]
        letra_usuario = dni[-1].upper()
        if letraCal == letra_usuario:
            return True
        else:
            return False
        
while True:
    print("STUDENT CRUD")
    print("-------------------------")
    print("1.- Add a student")
    print("2.- Delete a student")
    print("3.- Modify a student")
    print("4.- Search a student")
    print("5.- Exit")
    option=input("Choose option: ")

    if option == "5":
        break

    if option == "1":
        dni=input("Give me a student dni: ")
        if controlDni(dni) == True:
            name=input("Give me a student name: ")
            surname=input("Give me a student surname: ")
            age=input("Give me a student age: ")
            city=input("Give me a student city: ")
            province=input("Give me a student province: ")
            email=input("Give me a student email: ")
            if controllerStudent.addStudent(dni,name,surname,age,city,province,email):
                print("Student created")
            else:
                print("This dni is allready exist")
        else:
            print("The leter in the DNI " +dni +" is not correct.")

    if option =="2":
        dni=input("Give me a student dni: ")
        if controllerStudent.delStudent(dni) is not None:
            print("Student has been eliminated")
        else:
            print("Student with this DNI does not exist.")

    if option=="3":
        dni=input("Give me a student dni: ")
        student=controllerStudent.search_student(dni)
        if student is not None:
            print("1.- Modify Age")
            print("2.- Modify City")
            print("3.- Modify Province")
            print("4.- Modify Email")
            opt=input("What do you want to modify: ")
            if opt == "1":
                newValue=input("Enter the new age: ")
                controllerStudent.modStudent(student,opt,newValue)
            elif opt == "2":
                newValue=input("Enter the new city: ")
                controllerStudent.modStudent(student,opt,newValue)
            elif opt == "3":
                newValue=input("Enter the new province: ")
                controllerStudent.modStudent(student,opt,newValue)
            elif opt == "4":
                newValue=input("Enter the new email: ")
                controllerStudent.modStudent(student,opt,newValue)
            print("Student has been modify")
        else:
            print("Student with this DNI does not exist.")

    if option == "4":
        dni=input("Give me a student dni: ")
        student=controllerStudent.search_student(dni)
        if student is not None:
            print("Student found with DNI:", student.get_dni())
            print("Name:", student.get_name()," Surnames:", student.get_surnames()," Age:", student.get_age()," City:", student.get_city()," Province:", student.get_province()," Email:", student.get_email())
        else: 
            print("Student with this DNI does not exist.")




















