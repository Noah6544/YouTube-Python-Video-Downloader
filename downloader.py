from pytube import YouTube
import time
import random



def download():
    print("\n")
    dir = input(r"ENTER THE DIRECTORY YOU WANT THE FILE TO BE DOWNLOADED INTO: ")
    print("\n")
    while True:
        try:
            link = input("ENTER THE YOUTUBE LINK OF THE VIDEO YOU WANT TO DOWNLOAD: ")
            #yt = YouTube(link).streams.first().download()
            yt = YouTube(link)
            correct = input("\nTHE TITLE OF THIS VIDEO IS: \" " + str(yt.title) + "\"  IS THIS CORRECT? (y/n):\n ")
            if correct == "y":
                print("\nDOWNLOADING...")
                yt.streams.filter(progressive=True).last().download(dir)                
                print("\nDOWNLOAD COMPLETE\n")
                YES = input("DO YOU WANT TO DOWNLOAD ANOTHER VIDEO? (y/n): \n")
                if YES == "y":
                    continue
                elif YES == "n":
                    break
                else:
                    print("AN ERROR OCCURED, RUN AGAIN\n")
            elif correct == "n":
                continue
            else:
                print("INVALID INPUT")

        except:
            print("\nINVALID INPUT\nTRY AGAIN\n")


download()
