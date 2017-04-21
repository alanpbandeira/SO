import threading
import math

from multiprocessing.pool import ThreadPool
from threading import Thread, Semaphore


def word_count(w_array):
    """
    Função responsável por contar a ocorrência 
    de uma palavra em um dado array.
    """
    wc = {}

    for word in w_array:
        word = word[0].lower() + word[1:]

        if not wc.keys() or word not in wc.keys():
            wc[word] = 1
            continue

        wc[word] += 1

    return wc

# Abre um arquivo de texto.
# coloca todas as palavras em uma lista.
fhand = open('text.txt', 'r')
text = fhand.read().split()

# Seta o numero inicial de threads.
n_threads = 4

# Avalia se todas as palavras podem ser 
# dividas igualmente por todas as threads, 
# caso não uma thread a mais será criada.
if len(text) % n_threads == 0:
    worker_words = len(text) / n_threads
else:
    worker_words = len(text) // n_threads
    n_threads += 1

# Inicia uma pool para guardar os valores 
# retornados pelas pelas threads.
pool = ThreadPool(processes=n_threads)

# Processa cada palavra removendo caracteres não
# alfabéticos no início ou um das palavras.
for idx in range(len(text)):
    if not text[idx][0].isalpha():
        text[idx] = text[idx][1:]

    if not text[idx][-1].isalpha():
        text[idx] = text[idx][:-1]

# Lista que guardará os pedaços do 
# array de palavras.
data = []

# Para o dado número de palavras por thread, 
# divide o array de paravras e aramazena em data.
for x in range(0, len(text), worker_words):
    t_words = text[x:x+worker_words]
    data.append(t_words)

# Executa todas as threads para cada 
# segmento do texto e armazena os resultados.
result = pool.map(word_count, data)

# Estrutura para contabilizar todas as ocorrências 
# em todos os segmentos do texto.
words_total = {}

# Computa a ocorrência de todas as palavras 
# em todos os segmentos.
for word in text:
    word = word[0].lower() + word[1:]

    if word not in words_total.keys():
        words_total[word] = 0
        
        for acc in result:
            words_total[word] += acc.get(word, 0)

# Imprime a ocorrência de uma dada palavra
print(words_total["dolor"])