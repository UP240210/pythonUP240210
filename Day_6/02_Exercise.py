# 1.- Unpack siblings and parents from family_members
Brothers = "Ikal", "Samuel", "Benjamin"
Sisters = "Yaretzi", "Perla"
siblings = Brothers + Sisters
mom = "Yazmín"
dad = "Juan Manuel"

family_members = siblings + (dad, mom)

*siblings_unpacked, dad_unpacked, mom_unpacked = family_members
print("Siblings:", siblings_unpacked)
print("Father:", dad_unpacked)
print("Mother:", mom_unpacked)
# Or, if you want the siblings as a tuple again:
siblings_tuple = family_members[:-2]
father_unpacked2 = family_members[-2]
mother_unpacked2 = family_members[-1]
print("Siblings as tuple:", siblings_tuple)
mom = "Yazmín"
dad = "Juan Manuel"
#------------------------------------------------------------
# 2.- Fruits
fruits = ("Apple", "Banana", "Orange", "Grape")
vegetables = ("Carrot", "Broccoli", "Spinach", "Tomato")
animal_products = ("Chicken", "Beef", "Milk", "Eggs")
food_stuff_tp = fruits + vegetables + animal_products
print(food_stuff_tp)
#------------------------------------------------------------
# 3.- List
food_stuff_lt = list(food_stuff_tp)
print(food_stuff_lt)
#------------------------------------------------------------
# 4.- Slice out
length_tp = len(food_stuff_tp)
middle_index_tp = length_tp // 2 

# For food_stuff_lt (list):
length_lt = len(food_stuff_lt)
middle_index_lt = length_lt // 2

if length_lt % 2 == 0:
    middle_items_lt = food_stuff_lt[middle_index_lt - 1:middle_index_lt + 1]
else:
    middle_items_lt = food_stuff_lt[middle_index_lt:middle_index_lt + 1]

print("Middle items (list):", middle_items_lt)
#------------------------------------------------------------
# 5.- Slice out the first three items and the last three items from food_staff_lt list
food_stuff_tp = fruits + vegetables + animal_products
food_stuff_lt = list(food_stuff_tp)

first_three = food_stuff_lt[:3]
last_three = food_stuff_lt[-3:]

print("First three:", first_three)
print("Last three:", last_three)
#------------------------------------------------------------
# 6.- Delete
del food_stuff_tp
try:
    print(food_stuff_tp)
except NameError:
    print("food_stuff_tp has been deleted.")
#------------------------------------------------------------
# 7.- Check item
if 'Banana' in food_stuff_lt:
    print("'Banana' is on the list")
else:
    print("'Banana' is not in the list")