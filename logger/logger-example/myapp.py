# import logging
# import mylib


# def main():
#     logging.basicConfig(filename='myapp.log', level=logging.INFO)
#     logging.info('Started')
#     mylib.do_something()
#     logging.info('Finised')

# if __name__ == "__main__":
#     main()


import logging
logging.basicConfig(filename='myapp.log', format='%(asctime)s %(message)s')
logging.warning('is when this event was logged.')