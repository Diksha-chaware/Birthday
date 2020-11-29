#time module is must reminder
#is set with the help of dates
import time
#os module is used to notify the user 
import os
#birthday file is a file in which month and date is present
birthdayFile = ' /path/to/birthday/:
def checkTodaysBirthday ():
  fileName = open(birthdayFile,today = time. strftime( '%m%d' )
                  flag = 0
                  for line in fileName :
                  if today in line :
                  line = line.split(' ')
                  flag =1
                  #line[1] contains Name
                  os.system('notify-send + ' ' + line[2] + '"' )
                            if flag ==0 :
                            os.system('notify-send if __name__ == '__main__' :)
                                      checkTodaysBirthday()

