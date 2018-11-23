"""
        
   created: mcclayac
   Company Name : BigMAN Software
   MyName: Tony McClay
   date: 11/22/18
   day of month: 22
   
   Project Name: 20PythonLibraries
   filename:  
   package name: 
   IDE: PyCharm
   
   
"""

import sched
import time
from datetime import datetime, timedelta

scheduler = sched.scheduler(timefunc=time.time)

def saytime():
    print(time.ctime())
    scheduler.enter(10, priority=0, action=saytime)

saytime()
try:
    scheduler.run(blocking=True)
except KeyboardInterrupt:
    print('Stopped.')

