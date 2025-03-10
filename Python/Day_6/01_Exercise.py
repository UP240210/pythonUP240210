# 1.- Create an empty tuple
empty_tuple = ()
#------------------------------------------------------------
# 2.- Create a tuple containing names of your family
siblings = "Yaretzi", "Ikal", "Samuel", "Benjamin", "Perla"
#------------------------------------------------------------
# 3.- Join family
Brothers = "Ikal", "Samuel", "Benjamin"
Sisters = "Yaretzi", "Perla"
show_family = Brothers + Sisters
print (show_family)
#------------------------------------------------------------
# 4.- How many people
number_siblings = len(siblings)
print (f"I have {number_siblings} siblings.")
#------------------------------------------------------------
# 5.- Family
mom = "Yazmín"
dad = "Juan Manuel"
family = (mom, dad) + show_family
print (f"My mom is: {mom}, my dad is: {dad}, and my siblings are: {show_family}")
print ("So my family is ")
