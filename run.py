import datetime as datetime
import scour
import reusables
import schedule


def run():
    r = input("Do you want to run this program: Y/N?")
    if r == "y" or "Y":
        scour.search()
    else:
        print("Maybe later? See You")
        print("love you")

run()
schedule.every(1).minute.do(run())
