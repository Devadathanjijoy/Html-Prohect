#no 1
#-----
#import itertools

#code = """
#def greet(name):
#    print(f"hello you f****ing NI****a,{name}")
        
        
#greet("Rahul")
#"""

#exec(code)

#no 2
#-----
#from functools import reduce

#def divition(a,b):
#    div = a / b 
#    return div

#num = [1,2,3,4,5,6]

#print(reduce(divition , num))



#no 3
#-----

#word = input("Enter the word")
#length = int(input())

#import itertools
#print(f"All possible combinations of the word {word} for the given input of {length} is {["".join(w) for w in list(itertools.combinations(word , length))]}")

#no 3
#-----

class Doctor():

    doctors_dict={}
    def __init__(self,name,emp_id,salary,specialisation):
        self.__name = name
        self.__emp_id = emp_id
        self.__salary = salary
        self.__specialisation = specialisation

        Doctor.add_doctor(self,name,specialisation)

    def get_name(self):
        return self.__name.title()
    def get_emp_id(self):
        return self.__emp_id
    def get_salary(self):
        return self.__salary
    def get_specialisation(self):
        return self.__specialisation
    
    def salary_update(self,new_salary):
        return self.__salary == new_salary
    

    @classmethod
    def add_doctor(cls,name,specialisation):
        cls.doctors_dict[name.title()]=specialisation.title()
    @classmethod
    def display_doctors(cls):
        return cls.doctors_dict
    
class Patients():

    patients_dict = {}
    def __init__(self,name,age,disease):
        self.__name =name
        self.__age = age
        self.__disease = disease

        Patients.add_patients(self,name,disease)

    def get_name(self):
            return self.__name.title()
    def get_age(self):
            return self.__age
    def get_disease(self):
            return self.__disease
        
    @classmethod
    def add_patients(cls,name,disease):
        cls.add_patients[name.title()]=disease.title()
    @classmethod
    def display_patients(cls):
            return cls.patients_dict
        
while True:
    print("""
        1:Display List for all Doctors
        2:Display List for all Patients
        3:Add a Doctor
        4:Add a Patient
        9:Quit
        """
    )
    val = int(input("enter 1 , 2 , 3 , 4 , 9 : "))
    while val not in [1,2,3,4,9]:
        val=int(input("enter 1 , 2 , 3 , 4 or 9: "))
    if val == 1:
        print(Doctor.display_doctors())
    elif val == 2:
        print(Patients.display_patients())
    elif val == 3:
        print(Doctor.add_doctor(input("Name of  new doctor: "),input("Doctor's specialisaton: ")))
    elif val == 4:
        print(Patients.add_patients())
    elif val == 9:
        break
    else:
        print("Invalid Inputs")