import threading
import math

from multiprocessing.pool import ThreadPool
from threading import Thread, Semaphore

fhand = open('text.txt', 'r')
text = fhand.read().split()

threads = []
n_threads = 4
pool = ThreadPool(processes=n_threads)

if len(text) % n_threads == 0:
    worker_words = len(text) / n_threads
else:
    worker_words = len(text) // n_threads
    n_threads += 1


accounted = False

for idx in range(len(text)):
    if not text[idx][0].isalpha():
        text[idx] = text[idx][1:]

    if not text[idx][-1].isalpha():
        text[idx] = text[idx][:-1]


def word_count(w_array):
    wc = {}

    for word in w_array:
        word = word[0].lower() + word[1:]

        if not wc.keys() or word not in wc.keys():
            wc[word] = 1
            continue

        wc[word] += 1

    return wc

data = []

for x in range(0, len(text), worker_words):
    t_words = text[x:x+worker_words]
    data.append(t_words)

result = pool.map(word_count, data)

words_total = {}

for word in text:
    word = word[0].lower() + word[1:]

    if word not in words_total.keys():
        words_total[word] = 0
        
        for acc in result:
            words_total[word] += acc.get(word, 0)

print(words_total["dolor"])