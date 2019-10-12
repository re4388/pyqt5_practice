#


# don't run this!! will hang!!!

# while True:
#     try:
#         print('Run it....')
#     except:
#         print('exception happened...')


# you can use keyboard incepter!
# while True:
#     try:
#         print('Run it....')
#     except Exception:
#         print('exception happened...')



# 可以使用sys.exc_info()方法取得一個Tuple物件，該Tuple物件中包括了 1.例外的類型 2.例外訊息 3.traceback物件：
# import sys

# try:
#     raise 'error'
# except:
#     a,b,c  = sys.exc_info()
#     print(a)
#     print('===================')
#     print(b)
#     print('===================')
#     print(c)


# a = (1,2,3,4,5)
# print(a[:2])