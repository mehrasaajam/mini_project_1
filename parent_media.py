
import pytube

class Media:

    def __init__(self, type, name, director, score, url, duration, casts):
        self.type = type
        self.name = name
        self.director = director
        self.score = score
        self.url = url
        self.duration = duration
        self.casts = casts


    def edit(self, objects, sel_name):

        for x in objects:

            if x.name == sel_name:
                print("1: Name")
                print("2: Diractor")
                print("3: IMDB score")
                print("4: Url")
                print("5: Duration")
                print("6: Casts")

                if x.type == "series":
                    print("7: Number of episods")

                elif x.type == "clip":
                    print("8: Genre")

                a = int(input("Enter the number of item that you want change: "))
                b = input("Enter your edited: ")

                if a == 1:
                    x.name = b
                elif a == 2:
                    x.director = b
                elif a == 3:
                    x.score = b
                elif a == 4:
                    x.url = b
                elif a == 5:
                    x.duration = b
                elif a == 6:
                    x.casts = b
                elif a == 7:
                    x.num_of_epi = b
                elif a == 8:
                    x.genre = b
                
                print("Information updated successfully")
                break

        else:
            print("There is no media with this name!")


    def remove(self, objects, sel_name):
        
        for x in objects:

            if x.name == sel_name:

                if x.type == "series":
                    del x.num_of_epi
                elif x.type == "clip":
                    del x.genre

                del x.type
                del x.name
                del x.director
                del x.score
                del x.url
                del x.duration
                del x.casts
                
                print("The media has been successfully removed")
                break

        else:
            print("There is no media with this name!")

    
    def show_info(self, objects, sel_name):
        
        for x in objects:

            if x.name == sel_name:

                if x.type == "series":
                    print(x.type, "\t\t", x.name, "\t\t", x.director, "\t\t", x.score, "\t\t", x.url, "\t\t", x.duration, "\t\t", x.casts, "\t\t", x.num_of_epi)

                elif x.type == "clip":
                    print(x.type, "\t\t", x.name, "\t\t", x.director, "\t\t", x.score, "\t\t", x.url, "\t\t", x.duration, "\t\t", x.casts, "\t\t", x.genre)

                elif x.type == "film" or x.type == "documentary":
                    print(x.type, "\t\t", x.name, "\t\t", x.director, "\t\t", x.score, "\t\t", x.url, "\t\t", x.duration, "\t\t", x.casts, "\t\t", x.num_of_epi, "\t\t", x.genre)
                break

        else:
            print("There is no media with this name!")


    def download(self, objects, sel_name):

        for x in objects:

            if x.name == sel_name:
                link = x.url
                first_stream = pytube.YouTube(link).streams.first()
                first_stream.download(output_path='./', filename='test.mp4')
                break

        else:
            print("There is no media with this name!")
        