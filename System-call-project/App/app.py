from .TernarySearchTree.ternary_search_tree import TST
from .SysCallProcessing.sc_descriptor import SCDescriptor
from . import file_operations as fo
from decimal import *


class App(object):
    """docstring for App."""
    def __init__(self, sc_log, max_gram):
        super(App, self).__init__()
        self.max_gram = max_gram
        self.descriptor = SCDescriptor(sc_log)
        self.data_base = {}
        self.scores = None

    def run(self):
        """docstring"""
        self.descriptor.run()
        call_ids = fo.extract_calls_id(self.descriptor.idx_file)
        self.fill_data_base(call_ids)
        self.scores = dict.fromkeys(list(range(1, self.max_gram+1)))

    def fill_data_base(self, call_sequence):
        """docstring"""
        self.init_db(self.descriptor.call_ids)

        for window in range(2, (self.max_gram + 1)):
            grams = fo.ngram_sequence(call_sequence, window)

            for gram in grams:
                self.data_base[gram[0]].put(gram, len(gram))

        print ("DB filled.")

    def init_db(self, call_ones):
        """
        Initialize the data_base with a a TST for each possible
        one_gram sequence.
        """
        for x in range(max([int(i) for i in call_ones]) + 1):
            if not self.data_base.keys() or x not in self.data_base.keys():
                self.data_base[str(x)] = TST()
                self.data_base[str(x)].put(str(x), True)

        print ("Syscall data base initialized.")

    def instace_query(self, root, gram_ssize):
        """
        Return all grams from the given root with the specified gram size.
        """
        pass

    def data_search(self, key):
        """
        Finds a provided key in the data_base, if no key is provided the
        complete data_base is returned
        """
        return self.data_base[key[0]].get(key.split(","))

    def gram_similarity(self, test_file):
        """docstring"""

        with open(test_file) as f:
            test = f.read().split()

            misses = 0
            upper_b = len(test)

            for gram in test:
                gram = gram.split(",")

                if gram[0] not in self.data_base.keys():
                    misses += 1
                elif self.data_base[gram[0]].get(gram):
                    continue
                else:
                    misses += 1

            score = misses / upper_b
            perc = int(score * 100)
            self.scores[len(test[0].split(","))] = (score, perc)

    def score_data_plot(self, set_size, test_file):
        """docstring"""

        with open(test_file) as f:
            test_data = f.read().split()

            upper_b = len(test_data)
            selected_data = []
            plot_data = {}

            if upper_b <= set_size:
                selected_data.append(test_data)
            else:
                for x in range((len(test_data) - set_size + 1)):
                    selected_data.append(test_data[x:x+1+set_size])

            for idx, data in enumerate(selected_data):
                misses = 0

                for gram in data:
                    gram = gram.split(',')

                    if gram[0] not in self.gram_base.keys():
                        misses += 1
                    elif self.gram_base[gram[0]].get(gram):
                        continue
                    else:
                        misses += 1

                score = misses / upper_b
                perc = Decimal(score) * Decimal(10) ** (-2)
                plot_data[i] = perc

        return plot_data
