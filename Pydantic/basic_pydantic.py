# def insert_patient_data(name,age):
#     print(name)
#     print(age)
#     print('inserted into database')

# insert_patient_data('saksham','twenty')

# def insert_patient_data(name: str,age: int):
#     print(name)
#     print(age)
#     print('inserted into database')

# insert_patient_data('saksham','30')

# def insert_patient_data(name: str,age: int):
#     if type(name)==str and type(age)==int:
#         print(name)
#         print(age)
#         print('inserted into database')
#     else:
#         raise TypeError('Incorrect data type')

# insert_patient_data('saksham',30)

# def insert_patient_data(name: str,age: int):
#     if type(name)==str and type(age)==int:
#         if age < 0:
#             raise ValueError('age cant be negative')  # data validation
#         else:
#             print(name)
#             print(age)
#             print('inserted into database')
#     else:
#         raise TypeError('Incorrect data type')

# insert_patient_data('saksham',30)

from pydantic import BaseModel

class Patient(BaseModel):
    name:str
    age:int

def insert_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print('inserted into database')

def update_patient_data(patient: Patient):
    print(patient.name)
    print(patient.age)
    print('updated into database')

patient_info = {'name':'Saksham', 'age':21}

patient1 = Patient(**patient_info)

insert_patient_data(patient1)