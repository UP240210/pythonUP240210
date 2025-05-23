# 1.- Add person dictionary
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
#---------------------------------------------------------------------------------
# 2.- Check if the person dictionary has skills key.
if 'skills' in person.keys():
    mid = int(len(person['skills'])/2)
    print(person['skills'][mid])
else:
    print(f"'skills' is not on the person")
#---------------------------------------------------------------------------------
# 3.- Check if the person dictionary has skills key.
if 'skills' in person.keys():
    if "Python" in person['skills']:
        print(f"Python is a skill in the diccionary")
    else:
        print(f"Python is not a skill in the diccionary")
else:
    print(f"'skills' is not on the person")
#---------------------------------------------------------------------------------
# 4.- If a person skills has only
fronDev = ['JavaScript','React']
backDev = ['Node','Python','MongoDB']
fullStack = ['React', 'Node', 'MongoDB']

if person['skills'] == fronDev:
    print(f"She's a front-end developer")
elif person['skills'] == backDev:
    print(f"She's a back-end developer")
elif person['skills'] == fullStack:
    print(f"She's a a fullstack developer")
else:
    print(f"unknown title")
#---------------------------------------------------------------------------------
# 5.- If the person is married and if he lives in Finland
if person['is_marred']:
    status = "She's married"
else:
    status = "She's not married"

print(f"{person['first_name']} {person['last_name']} lives in {person['country']}. {status} ")

