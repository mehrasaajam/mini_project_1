
from parent_media import Media
from film import Film
from series import Series
from documentary import Documentary
from clip import Clip

objects = []

def read_from_database():
    f = open("database.txt", "r")
    line = f.read().split("\n")

    for i in range (len(line)):

        result = line[i].split(",")

        if result[0] == "film":
            my_obj = Media(result[0], result[1], result[2], result[3], result[4], result[5], result[6])
        elif result[0] == "series":
            my_obj = Series(result[0], result[1], result[2], result[3], result[4], result[5], result[6], result[7])
        elif result[0] == "documentary":
            my_obj = Media(result[0], result[1], result[2], result[3], result[4], result[5], result[6])
        elif result[0] == "clip":
            my_obj = Clip(result[0], result[1], result[2], result[3], result[4], result[5], result[6], result[7])

        objects.append(my_obj)

    f.close()

def write_to_database(objects):
    f = open("database.txt", "w")

    for x in objects:

        if x.type == "film":
            f.write(x.type + "," + x.name + "," + x.director + "," + x.score + "," + x.url + "," + x.duration + "," + x.casts + "\n")
        elif x.type == "series":
           f.write(x.type + "," + x.name + "," + x.director + "," + x.score + "," + x.url + "," + x.duration + "," + x.casts + "," + x.num_of_epi + "\n")
        elif x.type == "documentary":
            f.write(x.type + "," + x.name + "," + x.director + "," + x.score + "," + x.url + "," + x.duration + "," + x.casts + "\n")
        elif x.type == "clip":
            f.write(x.type + "," + x.name + "," + x.director + "," + x.score + "," + x.url + "," + x.duration + "," + x.casts + "," + x.genre + "\n")
    
    f.close()


def show_menu():
    print("1: Add")
    print("2: Edit")
    print("3: Remove")
    print("4: Search")
    print("5: Show list")
    print("6: Show info")
    print("7: Download")
    print("8: Exit")

print("Welcome to media")
read_from_database()

while True:
    
    show_menu()
    choice = int(input("Enter your choice: "))

    if choice == 1:
        x = input("Enter type: ")
        if x == "film":
            Film.add(objects)
        elif x == "series":
            Series.add(objects)
        elif x == "documentary":
            Documentary.add(objects)
        elif x == "clip":
            Clip.add(objects)
 
    elif choice == 2:
        sel_name = input("Enter name: ")
        for x in objects:
            if x.name == sel_name:
                x.edit(objects, sel_name)

    elif choice == 3:
        sel_name = input("Enter name: ")
        for x in objects:
            if x.name == sel_name:
                x.remove(objects, sel_name)

    elif choice == 4:
        x = input("Enter type: ")
        if x == "film":
            Film.search(objects)
        elif x == "series":
            Series.search(objects)
        elif x == "documentary":
            Documentary.search(objects)
        elif x == "clip":
            Clip.search(objects)

    elif choice == 5:

        for x in objects:
            if x.type == "film":
                Film.show_list(objects)
            elif x.type == "series":
                Series.show_list(objects)
            elif x.type == "documentary":
                Documentary.show_list(objects)
            elif x.type == "clip":
                Clip.show_list(objects)

    elif choice == 6:
        sel_name = input("Enter name: ")
        for x in objects:
            if x.name == sel_name:
                x.show_info(objects, sel_name)

    elif choice == 7:
        sel_name = input("Enter name: ")
        for x in objects:
            if x.name == sel_name:
                x.download(objects, sel_name)

    elif choice == 8:
        write_to_database(objects)
        exit(0)

    else:
        print("Your choice should be between 1 to 8")
