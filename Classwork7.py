print('Lesson 8: Log and UnitTest')


import logging


logging.basicConfig(level=logging.ERROR, filename='pysenior.log', filemode='w',
                    format='time%(asctime)s:level%(levelname)s:description-%(message)s')

# logging.debug('log level debug')
# logging.info('log level info')
# logging.warning('log level warning')
# logging.error('log level error')
# logging.critical('log level critical')

logging.info('launch app')

numbers = [2, 5, 3, 1, 0, 7, 9, 8]

try:
    logging.error('treat list by cycle')
    for i in range(0, 10):
        print(f'index {i}: element{numbers[i]}')

except Exception as error:
    logging.error(error.__str__())
    print(error.__str__())
