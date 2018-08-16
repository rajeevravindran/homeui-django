import os

def startAlarm(date,song):
    currentDate = str(date.date().day)
    currentTime = str(date.strftime("%H:%M"))
    commandToExecute = "alarm -s %s %s %s" % (currentDate, currentTime, song)
    return commandToExecute
    # os.system(commandToExecute)