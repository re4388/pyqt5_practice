a =  int ( input ( ' a = ' ))
b =  int ( input ( ' b = ' ))
c =  int ( input ( ' c = ' ))



# way1
# if a > b:
#     the_max = a
# else :
#     the_max = b
# if c > the_max:
#     the_max = c
# print ( ' The max is: ' , the_max)


#way2 三元條件運算符
# the_max = a if a > b else b
# the_max = c if c > the_max else the_max
# print ( ' The max is: ' , the_max)


# way3 BIF
# print ( ' The max is: ' , max (a, b, c))


# readibility is key, which is all about reading code and maintain code is most of dev are doing
# don't reinvent the wheel
# 
# 
#  