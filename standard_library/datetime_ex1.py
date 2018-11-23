"""
        
   created: mcclayac
   Company Name : BigMAN Software
   MyName: Tony McClay
   date: 11/23/18
   day of month: 23
   
   Project Name: 20PythonLibraries
   filename:  
   package name: 
   IDE: PyCharm
   
   
"""

import datetime

dt = datetime.datetime.now()
dt_utc = datetime.datetime.utcnow()
difference = (dt - dt_utc).total_seconds()

print('Total difference: %.2f seconds' % difference)

dt = datetime.datetime.now(tz=datetime.timezone.utc)
print(str(dt))

print('------------------------------------')

import arrow

t0 = arrow.now()
print(t0)

t1 = arrow.utcnow()
print(t1)

difference = (t0 - t1).total_seconds()

print('Total difference: %.2f seconds' % difference)
