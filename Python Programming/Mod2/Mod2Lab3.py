#Alex Ferguson
#Python
#Mod 2 Lab 3
#Due: 04/12/2023



def generation_determiner():
    year = int(input("Enter your birth year: "))
    
    if year >= 2013:
        print("You are part of the alpha generation!")
    
    elif year >= 1997 and year <= 2012:
        print("You are part of Gen Z!")

    elif year >= 1981 and year <= 1996:
        print("You are a millennial!")

    elif year >= 1965 and year <= 1980:
        print("You are part of Gen X!")

    elif year >= 1946 and year <= 1964:
        print("You are a baby boomer!")

    else:
        print("You are ancient!")

generation_determiner()
generation_determiner()
generation_determiner()