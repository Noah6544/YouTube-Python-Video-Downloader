from pytube import YouTube
import time
import random


def timestuff():
    randomnum = random.randint(3, 9)
    for i in range(0, randomnum):
        randomnum = random.randint(1, 9)
        if randomnum == 1:
            print("PLEASE WAIT...")
        elif randomnum == 2:
            print("WORKING...")
        elif randomnum == 3:
            print("ALMOST THERE...")
        elif randomnum == 4:
            print("PREPARING DOWNLOAD...")
        # elif random > 4 and <= 7:
        # print("WAIT WHILE WE SET IT UP FOR YOU...")
        elif randomnum == 8:
            print("NEARLY!")
        elif randomnum == 9:
            print("IDK WAIT")


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
                yt.streams.filter(progressive=True).last().download(dir)
                print("\nDOWNLOADING...")
                print("\nDOWNLOAD COMPLETE\n")
                YES = input("DO YOU WANT TO DOWNLOAD ANOTHER VIDEO? (y/n): \n")
                if YES == "y":
                    continue
                elif YES == "n":
                    print("\nTHANKS FOR USING THIS PROGRAM, WRITTEN BY NOAH(not pytube)")
                    break
                else:
                    print("OOPS ERROR RUN AGAIN\n")
            elif correct == "n":
                continue
            else:
                print("INVALID INPUT")

        except:
            print("\nINVALID INPUT\nTRY AGAIN\n")


download()
