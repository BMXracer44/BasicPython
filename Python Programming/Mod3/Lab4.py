#Alex Ferguson
#Python
#Mod 3 Lab 4
#04/18/23

print("=====Genre Application=====")

genres  = []


def fill_genres():
    print("\nPlease enter the genres of music you like (type END to move on): ")
    user_genre = input("\tEnter a genre: ")

    while user_genre != 'END':
        genres.append(user_genre)
        user_genre = input("\tEnter a genre: ")

def list_genres():
    if len(genres) > 0:
        print(f"\nYou like {len(genres)} genres. Here they are: ")
        i = 1
        for genre in genres:
            if genre.lower() == "kpop":
                print(f"\t{i}. {genre}---but Jpop is better")
            else:
                print(f"\t{i}. {genre}")
            i += 1 
    else:
        print("\nYou need to enter some genres!")

def get_menu():
    print("\nMenu Options: ")
    print("\t1. Add genres ")
    print("\t2. List genres")
    print("\t3. Exit")
    return int( input("\tSelection: "))
    
menu_option = get_menu()

while menu_option != 3:
    if menu_option == 1:
        fill_genres()
    elif menu_option == 2:
        list_genres()
    elif menu_option > 3 or menu_option < 1:
        print("Enter a valid option!")
    menu_option = get_menu()