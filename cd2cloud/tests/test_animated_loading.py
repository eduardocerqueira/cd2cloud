import itertools
import threading
import time
import sys

done = False

def animate():
    """Animate loading loop"""
    for c in itertools.cycle(['|', '/', '-', '\\']):
        if done:
            break
        sys.stdout.write('\rloading ' + c)
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write('\rDone!     ')
    print

if __name__ == '__main__':
    t = threading.Thread(target=animate)
    t.start()
    # clock to stop the thread
    time.sleep(5)
    done = True
