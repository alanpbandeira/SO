from TernarySearchTree.ternary_search_tree import TST
from SysCallProcessing.sc_descriptor import SCDescriptor
from . import file_operations as fo

class App(object):
    """docstring for App."""
    def __init__(self, sc_log, max_gram):
        super(App, self).__init__()
        self.max_gram = max_gram
        self.descriptor = SCDescriptor(sc_log)
        self.data_base = {}

    def run(self):
        """docstring"""
        self.descriptor.run()
        call_ids = fo.extract_calls_id(self.descriptor.idx_file)
        self.fill_data_base(call_ids)


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
        for x in range(max([int(i) for i in call_sequence]) + 1):
            if not self.data_base.keys() or x not in self.data_base.keys():
                self.data_base[str(x)] = TST()
                self.data_base[str(x)].put(str(x), True)

        print ("Syscall data base initialized.")

    def instace_query(self, root, gram_ssize):
        """
        Return all grams from the given root with the specified gram size.
        """
        pass

    def data_search(self, key=None):
        """
        Finds a provided key in the data_base, if no key is provided the
        complete data_base is returned
        """
        return self.data_base[key[0]].get(key)

    def data_view(self):
        """docstring"""
        pass
