#!/usr/bin/python3

import datetime
import calendar
from datetime import date
import easygui
import time
import os

# time set for 10 minutes before the beginning of the class
# dictionary days in the format of 
# weekday of the class: time of 10 minutes before the time of class(24 hour clock)
days = {'Tuesday':'5:20',
        'Wednesday': '5:20',
        'Saturday': '21:20'}

def alert():
    rem_minutes = int(days[calendar.day_name[date.today().weekday()]].split(':')[1])+10 - datetime.datetime.now().minute
    message = "Ready for Class?\nClass in: " + str(rem_minutes) + " minutes."
    # set ready message and snooze button message 
    # first is ready button and second is snooze button
    # you can simply close the window to avoid any action
    choices = ['Yes, start my Skype', 'Remind me after 2 minutes']
    # display an alert box to draw attention and remind the user
    res = easygui.ynbox(message, "Class Alert", choices)
    if res:
        return True
    else:
        time.sleep(120) # snooze time 2 minutes --> 2 * 60(seconds) = 120 seconds
        alert() # regenerate the alert if snoozed

def chk_time():
    today_time = days[calendar.day_name[date.today().weekday()]]
    its = today_time.split(':')
    hour = its[0]
    minutes = its[1]
    if hour == str(datetime.datetime.now().hour) and minutes == str(datetime.datetime.now().minute):
        return True
    else:
        time.sleep(60) # if time doesn't match, wait for a minute and recheck
        chk_time()


# check if today is the day for class
def chk_imp(day = ""):
    if day in days.keys():
        return True
    time.sleep(86400) # if it is not the required day, sleep for another day, then check it again
    chk_imp(calendar.day_name[date.today().weekday()])

def main(): # program begins here and never ends
    while True: # is always running
        day_today = calendar.day_name[date.today().weekday()] # today's day
        imp = chk_imp(day_today)
        if (imp):
            today_time = days[day_today]
            its = today_time.split(':')
            hour = its[0]
            #minutes = its[1]
            if hour >= str(datetime.datetime.now().hour): # check if class can still be managed.
                if (chk_time()):
                    if (alert()): #generate alert and check the response
                        os.system('skype') 
                        # you can write any other command or simply comment out the box to write your own
        time.sleep(900) # sleeps for 15 minutes

        

if __name__ == '__main__':
    main()
