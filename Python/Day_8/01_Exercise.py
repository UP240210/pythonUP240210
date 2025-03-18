# 1.- Create an empty dictionary.
dog = {}
#----------------------------------------------------------------
# 2.- Add name, color, breed, legs, age to the dog dictionary.
dog = {'name':'Pelusa',
    'color':'Black',
    'breed':'House cat',
    'legs':4,
    'age':11}
#----------------------------------------------------------------
# 3.- Create a student dictionary.
student = {
    'complete_name':'Perla RUbi',
    'last_name':'Rodriguez',
    'gender':'Female',
    'age':19,
    'marital_status':'In a relationship',
    'skills':['Drawing','Teaching','Playing VD','Sing','Optimism'],
    'country':'Mexico',
    'city':'Guanajuato',
    'addres':{
        'street':'Baker Street',
        'zipcode':'NW1 6XE',
    }
}
#----------------------------------------------------------------
# 4.- Length.
print(f'The lenght of the student dictionary is {len(student)}')
#----------------------------------------------------------------
# 5.- Type.
print(f'The data type of student skills is {type(student["skills"])}')
#----------------------------------------------------------------
# 6.- Modify the skills.
student['skills'].append('PHP')
print(student['skills'])
#----------------------------------------------------------------
# 7.- Get the sictionary keys as list.
keyList = list(student.keys())
print(keyList)
#----------------------------------------------------------------
# 8.- Get the sictionary values as a list.
valList = list(student.values())
print(valList)
#----------------------------------------------------------------
# 9.- Change the dictionary to a list of tuples using items().
studentTuple = student.items()
print(studentTuple)
#----------------------------------------------------------------
# 10.- Delete one of the items in the dictionary.
student.pop('gender')
print(student)
#----------------------------------------------------------------
# 10.- Delete dictionaries.
del dog, student