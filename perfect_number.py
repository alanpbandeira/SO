import threading
from threading import Thread, BoundedSemaphore, Semaphore
import math

factor_buffer = []
perfect = False
checked = False

w_semaphore = Semaphore(0)
c_semaphore = Semaphore()

number = int(input("Enter candidate number:"))
n_threads = int(input("Enter the number of working threads:"))

checking = [1 for x in range(n_threads)]

def perfection_check():
    global factor_buffer, number, checking, checked, w_semaphore, perfect
    
    w_semaphore.acquire()

    total = sum(factor_buffer)
    if total > 1 and (total+1) == number:
        perfect = True

    checked = True

def factor_check(search_data):
    global factor_buffer, number, checking, c_semaphore, w_semaphore
    
    for element in search_data:
        if number % element == 0:
            factor_buffer.append(element)

    c_semaphore.acquire()
    
    try:
        checking.pop()
    except:
        pass

    if not checking and w_semaphore._value == 0:
        w_semaphore.release()
    
    c_semaphore.release()

try:
    threading._start_new_thread(perfection_check, ())
except:
    print("Unable to create perfection checker.")
    exit()

search_elements = list(range(number))[2:]
t_elements = math.floor(len(search_elements) / n_threads)
working_threads = []

for x in range(0, len(search_elements), t_elements):
    data = search_elements[x: x + t_elements]
    try:
        working_threads.append(Thread(None, factor_check, None, (data, )))
    except:
        print("Could not create working thread.")

for worker in working_threads:
    worker.start()

while not checked:
    pass

print(perfect)