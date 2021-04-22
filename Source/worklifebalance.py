from datetime import date
from datetime import datetime
import os
import sys
import ctypes 
config_name = 'myapp.cfg'
today = date.today()
weekday=today.weekday()
now = datetime.now()
hour=now.hour

config_path = os.path.realpath(os.path.dirname(sys.argv[0]))
#determine if application is a script file or frozen exe
if getattr(sys, 'frozen', False):
    config_path += '\\AppsToLaunch\\'
elif __file__:
    config_path += '\\dist\\AppsToLaunch\\'

applist=[]
apps=os.listdir(config_path)

for app in apps:
    directpath=config_path + app
    applist.append(directpath)
    

if(weekday<5 and hour <17 and hour >7):   
     for dirs in applist:
         os.startfile(dirs)

#debug
# testcommentchange


