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

   format example and parse datetime
   
"""

import parsedatetime as pdt

cal = pdt.Calendar()

examples = [
    "2016-07-16",
    "2016/07/16",
    "2016-7-16",
    "2016/7/16",
    "07-16-2016",
    "7-16-2016",
    "7-16-16",
    "7/16/16",
]

print('{:30s}{:>30s}'.format('Input', 'Result'))
print('=' * 60)
# for e in examples:
#     dt, result = cal.parseDT(e)
#     print('{:<30s}{:>30}'.format('"' + e + '"', dt.ctime()))

for e in examples:
    dt, result = cal.parseDT(e)
    print('{:<30s}{:>30}'.format('"' + e + '"', dt.ctime()))
