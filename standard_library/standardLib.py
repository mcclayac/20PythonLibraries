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
import collections
from string import ascii_lowercase

dict(zip(ascii_lowercase, range(4)))


def fetch_data():
    return 42, 'jsmith', 'John', 'Smith'


# UserRecord = collections.namedtuple("UserRecord", ('user_id', 'username', 'first_name', 'last_name'))


def fetch_data2():


    UserRecord = collections.namedtuple("UserRecord", ('user_id', 'username', 'first_name', 'last_name'))
    return UserRecord(42, 'jsmith', 'John', 'Smith')


def exNamedTuples():
    result = fetch_data2()

    print("user id : {}  username : {}  first name : {}".
          format(result.user_id, result.username, result.first_name))

exNamedTuples()

def f():
    # Return a namedtuple!
    A = collections.namedtuple("A", ('count', 'enabled', 'color'))
    return A(2, False, "blue")

count, enabled, color = f()

print("count : " + str(count))
print("enabled : " + str(enabled))

result = f()
print("count : {}".format(result.count))


import logging
logger = logging.getLogger()

def exlogging():

    logger = logging.getLogger(__name__)
    logger.debug('This is for debugging. Very talkative!')
    logger.info('This is for normal chatter')
    logger.warning('Warnings should almost always be seen.')
    logger.error('You definitely want to see all errors!')
    logger.critical('Last message before a program crash!')
    secret_parameter = 'Tony McClay'

    logger.debug("Going to perform magic with '%s'", secret_parameter)

print("Example Logging")
print("-------------------------------------------------")
exlogging()


def exlogging2():
    import logging
    log = logging.getLogger("my-logger")
    # log = logging.getLogger(__name__)
    log.info("Hello, world")


exlogging2()



# Bottom of the file
if __name__ == '__main__':
    logging.basicConfig(level="INFO")
    # logging.basicConfig(level=logging.DEBUG)

