# 1.- Concatenate the string
from functools import reduce
palabras = ['Thirty', 'Days', 'Of', 'Python']
resultado1 = reduce(lambda x, y: x + ' ' + y, palabras)
print(resultado1)
#------------------------------------------------------------
# 2.- Concatenante in a single string
from functools import reduce
palabras = ['Coding', 'For', 'All']
resultado = reduce(lambda x, y: x + ' ' + y, palabras)
print(resultado)
#------------------------------------------------------------
# 3.- Declare a variable
company = "Coding For All"
#------------------------------------------------------------
# 4.- Print the variable company using print().
print("Lo que tiene la variable company es:", company)
#------------------------------------------------------------
# 5.- Print the lenght of the company string
print (len(company))
#------------------------------------------------------------
# 6.- Change all the characters using uppercase
upper2 = "hola mundo"
print ("Upper:", upper2.upper())
#------------------------------------------------------------
# 7.- Change all the characters using lower
lower2 = "HOLA MUNDO"
print ("Lower:", lower2.lower())
#------------------------------------------------------------
# 8.-  Use capitalize(), title(), swapcase()
print (f"Capitalize: {company.capitalize()}\nTitle: {company.title()}\nSwapcase: {company.swapcase()}")
#------------------------------------------------------------
# 9.- Cut(slice) out the first word
text = "Coding For All"
words = text.split()
remaining_text = " ".join(words[1:]) #Une las palabras desde el segundo elemento en adelante.
print(remaining_text)
#------------------------------------------------------------
# 10.- Cut(slice) out the first word
Contains = "Coding For All"
if Contains in text:
    print("The string contains the word 'Coding'")
else:
    print("The string doesn't contain the word 'Coding'")
#------------------------------------------------------------
# 11.- Remplace Coding to coding
Change = "coding For All"
if Change in text:
    print("The string contains the word 'Coding'")
else:
    print("The string doesn't contain the word 'Coding'")
#------------------------------------------------------------
# 12.- Change Python For Everybody to Python For All
python_for_everyone = "Python for Everyone"

# Using the replace() method:
replace2 = python_for_everyone.replace("Everyone", "All")
print(replace2)  

# Using split() and join():
split = python_for_everyone.split()
split[2] = "All" #Replace the third word.
new_text = " ".join(split)
print(new_text) 

#Using slicing and concatenation.
new_text_slice = python_for_everyone[:11] + "All"
print(new_text_slice)
#------------------------------------------------------------
# 13.- Split the string 'Coding For All'
text = 'Coding For All'
variable_13 = text.split()
print(variable_13)
#------------------------------------------------------------
# 14.- Social medias
companies = "Facebook, Google, Microsoft, Apple, IBM, Oracle, Amazon"
company_list = companies.split(",")
print(company_list)
#------------------------------------------------------------
# 15.- First Character
first_character = text[0]
print(f"El primer caracter es: {first_character}")
#------------------------------------------------------------
# 16.- Last Character
first_character = text[13]
print(f"El ultimo caracter es: {first_character}")
#------------------------------------------------------------
# 17.- Character 10
first_character = text[10]
print(f"El caracter 10 es: {first_character}")
#------------------------------------------------------------
# 18.- Acronym
variable_18 = python_for_everyone.split()
acronym = ''.join(word[0].upper() for word in variable_18)
print(acronym)
#------------------------------------------------------------
# 19.- Acronym
variable_19 = text.split()
acronym = ''.join(word[0].upper() for word in variable_19)
print(acronym)
#------------------------------------------------------------
# 20.- Index
index_of_c = text.index("C")
print(index_of_c)
#------------------------------------------------------------
# 21.- Index 2 
index_of_c = text.index("F")
print(index_of_c)
#------------------------------------------------------------
# 22.- rfind
last_l_index = text.rfind("l")
print(last_l_index)
#------------------------------------------------------------
# 23.- find fist because
lk = 'You cannot end a sentence with because because because is a conjunction'
first_because = lk.find('because')
print(first_because)
#------------------------------------------------------------
# 24.- find last because
last_because = lk.rindex('because')
print(last_because)
#------------------------------------------------------------
# 25.- Slice out the word 'because'
start_index = lk.find('because because because')
end_index = start_index + len('because because because')
sliced_phrase = lk[start_index:end_index]
print(sliced_phrase)
#------------------------------------------------------------
# 26.- find the position
lk = 'You cannot end a sentence with because because because is a conjunction'
first_because = lk[0]
print(first_because)
#------------------------------------------------------------
# 28.- Substring
starts_with_coding = text.startswith('Coding')
print(starts_with_coding)
#------------------------------------------------------------
# 29.- Substring ends with
ends_with_coding = text.endswith('coding')
print(ends_with_coding)
#------------------------------------------------------------
# 30.- Cut spaces
spaces = '    Coding For All      '
stripped_text = spaces.strip()
print(stripped_text)
#------------------------------------------------------------
# 31.- WIch is true and false
variable_31 = ["30DaysOfPython", "thirty_days_of_python"]
for var in variable_31:
    is_identifier = var.isidentifier()
    print(f"'{var}' is an identifier: {is_identifier}")
#------------------------------------------------------------
# 32.- Libraries
libraries = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
joined_string = ' # '.join(libraries)
print(joined_string)
#------------------------------------------------------------
# 33.- Escape sequence
sentence1 = "I am enjoying this challenge."
sentence2 = "I just wonder what is next."
combined_sentences = sentence1 + "\n" + sentence2
print(combined_sentences)
#------------------------------------------------------------
# 34.- Escape sequence
sequence = "Name\tAge\tCountry\tCity\nAsabeneh\t250\tFinland\tHelsinki"
print(sequence)