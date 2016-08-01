import threading
from Queue import Queue

fibo_dict = {}
shared_queue = Queue()
input_list = [3, 10, 5, 7]

queue_condition = threading.Condition()

