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

# In [5]: history
# import psutil
# psutil.virtual_memory()
# psutil.swap_memory()
# psutil.disk_partitions()
# history

import psutil
# psutil.net_io_counters(pernic=True)


import psutil
import os, sys, time

pid = os.getpid()
p = psutil.Process(pid)
print('Process info:')
print('  name  :', p.name())
print('  exe   :', p.exe())

data = []
while True:
    data += list(range(100000))
    info = p.memory_full_info()
    # Convert to MB
    memory = info.uss / 1024 / 1024
    print('Memory used: {:.2f} MB'.format(memory))
    if memory > 40:
        print('Memory too big! Exiting.')
        sys.exit()
    time.sleep(1)

