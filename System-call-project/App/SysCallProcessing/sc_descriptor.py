from .. import file_operations as fo

class SCDescriptor(object):
    """docstring for SCDescriptor."""
    def __init__(self, log_file):
        super(SCDescriptor, self).__init__()
        self.log_file = log_file
        self.idx_file = None
        self.call_ids = None

    def run(self):
        self.idx_file, self.call_ids = fo.syscall_id(self.log_file)
