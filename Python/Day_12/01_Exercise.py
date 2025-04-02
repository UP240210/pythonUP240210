# 1.- Writ a function which generates a six digit/character random_user_id
import random as rd
import string

def random_user_id():
    word = ''
    char = string.ascii_letters + string.digits
    for i in range(6):
        x = rd.randint(0,len(char))
        word += char[x]
    return word
#------------------------------------------------------------------------------------------
# 2.- Modify the previous task. Declare a function named user_id_gen_by_user.
def user_id_gen_by_user():
    word = ''
    numChar = int(input("Enter the number of characters: "))
    numUser = int(input("Enter the number of user names: "))
    char = string.ascii_letters + string.digits
    for c in range(numUser):
        for i in range(numChar):
            x = rd.randint(0,len(char))
            word += char[x]
        print(word)
        word = ''
#------------------------------------------------------------------------------------------
# 3.- Write a function named rgb_color_gen. It will generate rgb colors.
def rgb_color_gen():
    r = rd.randint(0,255)
    g = rd.randint(0,255)
    b = rd.randint(0,255)
    rgb =  [r,g,b]
    return rgb

print(rgb_color_gen())
