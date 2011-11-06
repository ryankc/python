import time
a = int(raw_input("How many seconds should we count down from? "))
for i in range (a,0,-1):
    print i
    time.sleep(1)
print "sleeping"    
