import time
starttime=time.time()
while True:
    print ("do stuff")
    time.sleep(1.00 - ((time.time() - starttime) % 1.00))


