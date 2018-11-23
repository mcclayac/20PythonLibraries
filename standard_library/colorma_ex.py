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

from colorama import init, Fore, Back, Style
init(autoreset=True)

# messages = [
#     'blah blah blah',
#     (Fore.GREEN + Style.BRIGHT
#         + Back.MAGENTA + 'Alert!!!'),
#     'blah blah blah'
# ]

messages = [
    'blah blah blah',
    (Fore.GREEN + Style.BRIGHT + 'Alert!!!'),
    'blah blah blah'
]


for m in messages:
    print(m)
