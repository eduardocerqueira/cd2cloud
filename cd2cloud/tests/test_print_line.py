import sys
import time

def countdown2(t):
    for i in range(5):
        print "counter %d\r" % i,
        sys.stdout.flush()
        time.sleep(1)

if __name__ == '__main__':
    countdown2(3)
    print "\rDONE" + " " * 10
