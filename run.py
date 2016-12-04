import datetime as datetime
import scour


def run():
    r = input("Do you want to run this program: Y/N?")
    if r == "y" or "Y":
        scour.search()
    else:
        print("Maybe later? See You")


run()
