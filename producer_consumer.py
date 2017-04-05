import time

buffer_size = 100
buffer = []

def producer():
    global buffer

    while True:
        if len(buffer) >= buffer_size:
            time.sleep(1)
        
        buffer.append(1)
        
        if buffer:
            pass # wakeup consumer

def consumer():
    global buffer

    while True:
        if not buffer:
            time.sleep(1)
        
        buffer.pop()

        if not buffer:
            pass # wakeup produce
