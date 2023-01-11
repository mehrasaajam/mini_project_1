
from parent_media import Media

class Film(Media):
    
    def __init__(self, type, name, director, score, url, duration, casts):
        super().__init__(type, name, director, score, url, duration, casts)

    
    @staticmethod
    def add(objects):
        type = input("Enter type: ")
        name = input("Enter name: ")
        director = input("Enter director: ")
        score = input("Enter IMDB score: ")
        url = input("Enter url: ")
        duration = input("Enter duration: ")
        casts = input("Enter casts: ")
        objects.append(Film(type, name, director, score, url, duration, casts))

    @staticmethod
    def search(objects):
        print("1: Searching according to name")
        print("2: Searching according to duration")
        cho = int(input("Select 1 or 2: "))

        if cho == 1:
            sel_name = input("Enter name: ")

            for x in objects:

                if x.name == sel_name:
                    print(x.type, "\t\t", x.name, "\t\t", x.director, "\t\t", x.score, "\t\t", x.url, "\t\t", x.duration, "\t\t", x.casts)
                    break
            else:
                print("There is no media with this name!")

        elif cho == 2:
            a = int(input("Min duration (min): "))
            b = int(input("Max duration (min): "))
            i = 0
            for x in objects:

                if x.type == "film":
                    c = x.duration

                    if a <= int(c) <= b:
                        print(x.type, "\t\t", x.name, "\t\t", x.director, "\t\t", x.score, "\t\t", x.url, "\t\t", x.duration, "\t\t", x.casts)
                        i += 1
                
            if i == 0:
                print("There is no media with this duration!")

    @staticmethod
    def show_list(objects):
        print("Type\t\tName\t\tDirector\t\tScore\t\tUrl\t\tDuration\t\tCasts")
        for x in objects:
            if x.type == "film":
                print(x.type, "\t\t", x.name, "\t\t", x.director, "\t\t", x.score, "\t\t", x.url, "\t\t", x.duration, "\t\t", x.casts)