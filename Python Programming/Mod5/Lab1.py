#Alex Ferguson
#Mod 5 Lab 1
#Python
#5/2/2023

#Dictionaries hold multiple key-value pairs

#We cannot have duplicate keys
#Data-types can be different

#Dictionaries are created using curly brackets { }

county_pop = {
    "Milwaukee": 939123,
    "Dane": 555474,
    "Waukesha": 404332,
    "Brown": 267364,
    "Racine": 197379,
}

#You can index a dictionary by using the key
print(county_pop["Milwaukee"])

#You can add or update values by assigning to a new or existing key
county_pop["Outagamie"] = 189620
county_pop["Milwaukee"] = 1000000

#You can use the pop method to remove by key
county_pop.pop("Racine")


for c, p in county_pop.items(): 
    print(f"{c} County | Population: {p}")