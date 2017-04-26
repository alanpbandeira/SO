import threading
from threading import Thread, Semaphore
import math

# Buffer de fatores.
# Chaveador da condição de perfeição.
# Chaveador da condição de verificação.
factor_buffer = []
perfect = False
checked = False

# Semáforo para o verificador de perfeição.
# Semáforo para os verificadores de fatores.
w_semaphore = Semaphore(0)
c_semaphore = Semaphore()

# Entrada do número a ser verificado e do número 
# de threads a serem usadas para verificação.
number = int(input("Enter candidate number:"))
n_threads = int(input("Enter the number of working threads:"))

# Lista de threads checadoras de fatores que estão ativas.
checking = [1 for x in range(n_threads)]


def perfection_check():
    """
    Função que checa a condição de perfeição 
    dos elementos no buffer de fatores.
    """
    global factor_buffer, number, checking, checked, w_semaphore, perfect
    
    w_semaphore.acquire()

    total = sum(factor_buffer)
    if total > 1 and (total+1) == number:
        perfect = True

    checked = True

def factor_check(search_data):
    """
    Função que checa os possíveis fatores do número.
    """
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

# Cria a thread de verificação de perfeição.
try:
    threading._start_new_thread(perfection_check, ())
except:
    print("Unable to create perfection checker.")
    exit()

# Cria uma lista de números para verificar a condição de fator.
# Define o número de elementos por thread.
# Lista para armazenar as threads verificadoras de fatores.
search_elements = list(range(number))[2:]
t_elements = math.floor(len(search_elements) / n_threads)
working_threads = []

# Cria as threads cada uma com um pedaço da lista 
# de possíveis fatores.
for x in range(0, len(search_elements), t_elements):
    data = search_elements[x: x + t_elements]
    try:
        working_threads.append(Thread(None, factor_check, None, (data, )))
    except:
        print("Could not create working thread.")

# Inicializa cada thread verificadora de fatores
for worker in working_threads:
    worker.start()

# Loop que se encerra quando a thread que verifica 
# a confição de perfeição termina de executar.
while not checked:
    pass

# Exibe o resultado
print(perfect)