
# import time

# print (f"Start : {time.ctime()}") 
# time.sleep( 5 )
# print (f"End : {time.ctime()}")


import time 

counter = 10
while counter >= 0:
    time.sleep(1)
    print('1 sec shall pass')
    counter = counter - 1





# import sched, time

# s1 = sched.scheduler(time.time, time.sleep)

# def do_something(sc): 
#     print ("Doing stuff...")
#     s1.enter(1, 1, do_something, (sc,))

# s1.enter(1, 1, do_something, (s1,))
# s1.run()





# import sched, time

# s = sched.scheduler(time.time, time.sleep)

# def do_something():
#     print('from do_somthing', time.time())


# print(time.time())
# s.enter(3, 1, do_something)
# s.run()
# print(time.time())