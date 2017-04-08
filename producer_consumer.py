import time
import threading

item_count = 0
buffer_size = 100
buffer = []
chand = threading.Condition()

def producer(start_time):
    global buffer, chand, item_count

    while True:
        if item_count == buffer_size:
            chand.acquire()
            chand.wait()

        buffer.append(1)
        item_count += 1
        
        if item_count == 1:
            chand.acquire()
            chand.notify()

def consumer(start_time):
    global buffer, chand, item_count

    while True:
        if item_count == 0:
            print("at consumer: " + str(time.time()- start_time))
            chand.acquire()
            chand.wait()
        
        buffer.pop()
        item_count -= 1

        if item_count == buffer_size - 1:
            chand.acquire()
            chand.notify()

start = time.time()

try:
    threading._start_new_thread(producer, (start, ))
    threading._start_new_thread(consumer, (start, ))
except:
    print("Error, unable to start threads")

while 1:
    pass