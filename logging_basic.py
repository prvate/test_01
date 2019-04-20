import logging
import os

logger = logging.getLogger(__name__)
#logger.setLevel(logging.INFO)
logger.setLevel(level=logging.DEBUG)

#formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s')
formatter = logging.Formatter("%(asctime)s [%(levelname)s] (%(funcName)s() (%(filename)s : %(lineno)d))  | %(message)s")

file_handler = logging.FileHandler('employee_01.log')
file_handler.setFormatter(formatter)

logger.addHandler(file_handler)


class User:
    """A sample Employee class"""

    def __init__(self, first, last):
        self.first = first
        self.last = last
        logger.info('Created Employee: {} - {}'.format(self.fullname, self.email))

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def add(self, x, y):
      """Add Function"""
      s = x / y
      return s

    def open_file(self, file):
      if os.path.exists:
        print('-' * 50)
        with open(file, 'r', encoding='utf-8') as f:
          h = f.readlines()
          for enum, x in enumerate(h):
            print(enum, x)


us_1 = User('John', 'Smith')
us_2 = User('Corey', 'Schafer')
us_3 = User('Jane', 'Doe')

a = 1
b = 0
try:
  print(us_3.add(a, b))
except ZeroDivisionError as err:
  # if this happens, we will return 0
  logger.error('We attempted to divide by zero, setting result to 0 : \n')
  logger.error(err)
  logger.error('\n' + '=' * 40)
  result = 0
except:
  # something else has happened, so we reraise it
  logger.critical('An exception has occurred while executing module.function()', exc_info=True) 

try:
  emp_3.open_file('ala_.txt')
except FileNotFoundError as fnfe:
  logger.error('We attempted open file: \n')
  logger.error(fnfe)
  logger.error('\n' + '=' * 40)
except:
  # something else has happened, so we reraise it
  logger.critical('An exception has occurred while executing module.function()', exc_info=True) 
  



