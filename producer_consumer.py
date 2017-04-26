import time
import threading

# Número de elementos no buffer
# Tamanho máximo do buffer
# Buffer de elementos
item_count = 0
buffer_size = 100
buffer = []

# Objeto que implementa trava para condição de corrida
chand = threading.Condition()


def producer(start_time):
    """
    Função que implementa a thread produtor.
    """
    
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
    """
    Função que implementa a thread consumidor.
    """
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

# Armazena o tempo de início.
start = time.time()

# Inicializa as threads de produtor e consumidor.
try:
    threading._start_new_thread(producer, (start, ))
    threading._start_new_thread(consumer, (start, ))
except:
    print("Error, unable to start threads")

# Loop infinito para execução das threads.
while True:
    pass