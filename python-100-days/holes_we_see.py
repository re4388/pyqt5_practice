
# 那些年我們踩過的那些坑
# https://github.com/jackfrued/Python-100-Days/blob/master/%E7%95%AA%E5%A4%96%E7%AF%87/%E9%82%A3%E4%BA%9B%E5%B9%B4%E6%88%91%E4%BB%AC%E8%B8%A9%E8%BF%87%E7%9A%84%E9%82%A3%E4%BA%9B%E5%9D%91.md


# is比較的是兩個整數對象的id值是否相等，也就是比較兩個引用是否代表了內存中同一個地址。
# ==比較的是兩個整數對象的內容是否相等，使用==時其實是調用了對象的__eq__()方法。


# 在Python的整個生命週期內，任何需要引用這些整數對象的地方，都不再重新創建新的對象，
# 而是直接引用緩存中的對象。Python把頻繁使用的整數對象的值定在[-5, 256]這個區間，
# 如果需要這個範圍的整數，就直接從small_ints中獲取引用而不是臨時創建新的對象


# def main():
#     x = y = - 1
#     while True:
#         x += 1
#         y += 1
#         if x is y:
#             print(' %d is %d ' % (x, y))
#         else:
#             print(' Attention! %d is not %d ' % (x, y))
#             break

#     x = y = 0
#     while True:
#         x -= 1
#         y -= 1
#         if x is y:
#             print(' %d is %d ' % (x, y))
#         else:
#             print(' Attention! %d is not %d ' % (x, y))
#             break


# if __name__ == "__main__":
#     main()


############################################################################################


# Python內部為了進一步提高性能，凡是在一個代碼塊中創建的整數對象，
# 如果值不在small_ints緩存範圍之內，但在同一個代碼塊中已經存在一個值與其相同的整數對象了，
# 那麼就直接引用該對象
a = 257


# def  main ():
#     b =  257   #第6行
#     c =  257   #第7行
#     print (b is c)   # True
#     print (a is b)   # False
#     print (a is c)   # False

# import dis

# dis.dis(main)

# if __name__ == "__main__":
#     main()


############################################################################################




# scores = [[0] * 3] * 5
# print(scores)
# [[0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0], [0, 0, 0]]

# wrong!! 
# names = [ '關羽' , '張飛' , '趙雲' , '馬超' , '黃忠' ]
# subjs = [ '語文' , '數學' , '英語' ]
# scores = [[ 0 ] *  3 ] *  5
# for row, name in  enumerate (names):
#     print ( f'請輸入{name}的成績')
#     for col, subj in  enumerate (subjs):
#         scores[row][col] =  float ( input (subj +  ' : ' ))
#         print (scores)

# 程序中可以使用的內存從邏輯上可以為五個部分，
# 按照地址從高到低依次是：棧（stack）、堆（heap） 、數據段（data segment）、只讀數據段（static area）和代碼段（code segment）。
# 
# 其中，棧用來存儲局部、臨時變量，以及函數調用時保存現場和恢復現場需要用到的數據，
# 這部分內存在代碼塊開始執行時自動分配，代碼塊執行結束時自動釋放，通常由編譯器自動管理；
# 
# 堆的大小不固定，可以動態的分配和回收，因此如果程序中有大量的數據需要處理，這些數據通常都放在堆上，
# 如果堆空間沒有正確的被釋放會引發內存洩露的問題，而像Python、Java等編程語言都使用了垃圾回收機制來實現自動化的內存管理
# （自動回收不再使用的堆空間）。
# 
# 下面的代碼中，變量a並不是真正的對象，它是對象的引用，相當於記錄了對像在堆空間的地址，通過這個地址我們可以訪問到對應的對象；
# 同理，變量b是列表容器的引用，它引用了堆空間上的列表容器，而列表容器中並沒有保存真正的對象，它保存的也僅僅是對象的引用。


# 我們對列表進行[[0] * 3] * 5操作時，僅僅是將[0, 0, 0]這個列表的地址進行了複製，並沒有創建新的列表對象，
# 所以容器中雖然有5個元素，但是這5個元素引用了同一個列表對象

# a =  object ()
# b = [ ' apple ' , ' pitaya ' , ' grape ' ]

# correct!!
# names = [ '關羽' , '張飛' , '趙雲' , '馬超' , '黃忠' ]
# subjs = [ '語文' , '數學' , '英語' ]
# scores = [[]] *  5 
# for row, name in  enumerate (names):
#     print ( '請輸入%s的成績'  % name)
#     scores[row] = [ 0 ] *  3 
#     for col, subj in  enumerate (subjs):
#         scores[row][col] =  float ( input (subj +  ' : ' ))
#         print (scores)




############################################################################################






