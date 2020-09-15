from time import *
import beepy
import keyboard


print("this is pomodor \n note:if you want to stop it keep pressing the key 's'")


def timecounting(min):
    global sec
    sec = 0
    while True:
        print("minuts: ", min, " ", "seconds: ", sec)
        sleep(1)
        if sec == 0:
            if min != 0:
                min = min-1
                sec = 59
            else:
                break
        elif keyboard.is_pressed("s"):
            exit()
        else:
            sec = sec-1


def pomodor(min):
    print("work time")

    timecounting(min)

    beepy.beep(sound=5)
    Break(xy)


def Break(minut):
    print("break time")

    timecounting(minut)

    beepy.beep(sound=5)
    pomodor(xx)


xx = int(input("Enter how much minuts you want: "))
xy = int(input("Enter how much break do you want: "))


pomodor(xx)
