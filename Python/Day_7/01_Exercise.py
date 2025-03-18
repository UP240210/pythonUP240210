# 1.- Find the length of the set it_companies.
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
print(f"The lenght of it companies is {len(it_companies)}")
#-------------------------------------------------------------------------------------
# 2.- Add Twiter.
it_companies.add("Twitter")
print(it_companies)
#-------------------------------------------------------------------------------------
# 3.- Insert multiple IT.
it_companies.update(["Youtube","Linux","Opera"])
print(it_companies)
#-------------------------------------------------------------------------------------
# 4.- Remove one of the companies.
it_companies.discard("Facebook")
print(it_companies)
#-------------------------------------------------------------------------------------
# 5.- What is the difference between.
print(f"La diferencia entre discard() y remove es que remove no indica error,\nsi no encuentra el elemento en cambio remove() si indica error")