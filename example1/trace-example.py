
# https://blog.csdn.net/liao392781/article/details/81131849


# this simple give you the error content
# try:
#     1/0
# except Exception as e:
#     print(e)


# give you the error line, just like you usually see in error code
import traceback

try:
    1/0
except Exception as e:
    traceback.print_exc()

