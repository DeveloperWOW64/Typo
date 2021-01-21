import time
name=("Jupiter")
print("This is Typo, your digital assistant.\nWelcome. Initializing ...")
time.sleep(3.4)
doToday=input(f"What would you like to do today, {name}? ")
if doToday=="set a timer":
    howLongTimer=input("For how long? (in seconds) ")
    if howLongTimer:
        print("Okay, set.")
        time.sleep(f"{howLongTimer}")
        print("Ding a Ling a Ling! Your timer ended.")