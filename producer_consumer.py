import time
import threading
import math

count = 0
buffer_size = 100
buffer = []
chand = threading.Condition()

def producer(start_time):
    global buffer, chand, count

    while True:
        if len(buffer) == buffer_size:
            chand.acquire()
            chand.wait()
        
        if time.time() - start_time >= 1:
            if math.floor(time.time() - start_time) % 10 == 0:
                start_time = time.time()
                print(1)
        buffer.append(1)
        
        if buffer:
            chand.acquire()
            chand.notify()

def consumer():
    global buffer, chand

    while True:
        if not buffer:
            chand.acquire()
            chand.wait()
        
        buffer.pop()

        if not buffer:
            chand.acquire()
            chand.notify()

start = time.time()

try:
    threading._start_new_thread(producer, (start, ))
    threading._start_new_thread(consumer, ())
except:
    print("Error, unable to start threads")

while 1:
    pass