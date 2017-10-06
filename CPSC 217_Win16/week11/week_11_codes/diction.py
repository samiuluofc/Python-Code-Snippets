# A concept of key:value pair

cities = {"Calgary":988193, "Edmonton":730372, "Banff":6700, "Black Diamond":1900}

#uofc = {161:"samiul", 300:"kaniz", 23:"nobin", 78:"anik"}

cities["Airdrie"] = 28927
cities["Chestermere"] = 9564
cities["Cochrane"] = 13750
cities["Cochrane"] = 13751
cities["Okotoks"] = 17145


#print(uofc)
#print(cities)
#print(cities["Cochrane"])


#cities.pop("Cochrane") # deleting a key value pair
#print(cities)
#cities.clear() # remove all pairs
#print(cities)

for k in cities.keys():
    print(k)

for v in cities.values():
    print(v)
