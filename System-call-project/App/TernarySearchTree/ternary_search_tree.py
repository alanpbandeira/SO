import queue
from .node import Node

class TST(object):
    """docstring for TST."""
    def __init__(self):
        super(TST, self).__init__()
        self.root = None

    def put(self, key, value):
        self.root = self.put_item(self.root, key, value, 0)

    def put_item(self, node, key, value, index):

        c = key[index]

        if node == None:
            node = Node(c)

        if int(c) < int(node.character):
            node.left_node = self.put_item(node.left_node, key, value, index)
        elif int(c) > int(node.character):
            node.right_node = self.put_item(node.right_node, key, value, index)
        elif index < (len(key) - 1):
            node.mid_node = self.put_item(node.mid_node, key, value, index+1)
        else:
            node.value = value

        return node

    def get(self, key):
        node = self.get_item(self.root, key, 0)

        if node == None:
            return None

        return node.value

    def get_item(self, node, key, index):

        if node == None:
            return None

        c = key[index]

        if int(c) < int(node.character):
            return self.get_item(node.left_node, key, index)
        elif int(c) > int(node.character):
            return self.get_item(node.right_node, key, index)
        elif index < (len(key) - 1):
            return self.get_item(node.mid_node, key, index+1)
        else:
            return node

    def traverse_util(self, root, c_buffer, depth, str_len, results):
        if root is not None:
            self.traverse_util(
                root.left_node, c_buffer, depth, str_len, results)
            c_buffer[depth] = str(root.character)

            # Use the line below if you want to get only maximum depth keys
            # if not any([root.left_node, root.right_node, root.mid_node]):
            if root.value and depth == str_len:
                print(depth, str_len)
            # if root.value:
            # if depth == str_len:
            #     print("here")
                # results.append("".join(c_buffer[:depth+1]))
                results.append("".join(c_buffer))
                # print(results)
                # print("".join(c_buffer[:depth+1]))

            self.traverse_util(
                root.mid_node, c_buffer, depth+1, str_len, results)

            self.traverse_util(
                root.right_node, c_buffer, depth, str_len, results)

    def traverse(self, str_size, max_gram):
        buf = [''] * max_gram
        results = []
        self.traverse_util(self.root, buf, 0, str_size, results)
        return results
