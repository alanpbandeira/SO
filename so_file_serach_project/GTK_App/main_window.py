import gi
import os
import platform
import subprocess
import numpy as np
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class MainWindow(Gtk.Window):
    """docstring for MainWindow."""
    def __init__(self):
        super(MainWindow, self).__init__(title="myapp")
        self.set_border_width(10)
        self.set_default_size(500, 300)

        # Vbox
        self.base_layout = Gtk.Box(
            orientation=Gtk.Orientation.VERTICAL, spacing=8)
        self.add(self.base_layout)

        # VBox row one
        self.row_one = Gtk.Box(
            orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

        # Row_one's Label_one
        self.label_one = Gtk.Label()
        self.label_one.set_label("Search String 1:")
        self.row_one.pack_start(self.label_one, False, True, 0)

        # Entry one
        self.entry_one = Gtk.Entry()
        self.row_one.pack_start(self.entry_one, False, True, 0)

        # Row_one's Label_twp
        self.label_two = Gtk.Label()
        self.label_two.set_label("Search String 2:")
        self.row_one.pack_start(self.label_two, False, True, 0)

        # Entry two
        self.entry_two = Gtk.Entry()
        self.row_one.pack_start(self.entry_two, False, True, 0)

        # Row_one's Search Button
        self.s_btn = Gtk.Button(label="search")
        self.s_btn.connect("clicked", self.run_search)
        self.row_one.pack_start(self.s_btn, False, True, 1)

        self.base_layout.pack_start(self.row_one, False, True, 0)

        # Vmox row two
        self.row_two = Gtk.Box(
            orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        self.base_layout.pack_start(self.row_two, True, True, 0)


    def run_search(self, widget):
        s_str_one = self.entry_one.get_properties("text")[0].lower()
        s_str_two = self.entry_two.get_properties("text")[0].lower()

        if (s_str_one == "" and s_str_two == ""):
            return

        pdf_files = pdf_search()

        if not pdf_files:
            print("No pdf file found.")
            return

        results = substring_search(pdf_files, s_str_one, s_str_two)


        # print(self.entry_one.get_properties("text")[0])

    def show_search_results(slef, data):
        """
        :param data: List of tuples
        """
        data_list_store = Gtk.ListStore(str, int, str)
        for item in data:
            data_list_store.append(list(item))

        data_tree_view = Gtk.TreeView(data_list_store)
        column_names = ["File/Directory", "Ocurrences", "Score"]
        for i, col_title in enumerate(column_names):

            rederer = Gtk.CellRendererText()
            column = Gtk.TreeViewColumn(col_title, renderer, text=i)
            data_tree_view.append_collumn(column)

        self.row_two.pack_start(data_tree_view, True, True, 0)
        pass

    @staticmethod
    def pdf_search():
        """
        :return results: list of strings for every pdf file found.
        """
        results = []

        for dirname, dirnames, filenames in os.walk('/'):
            for filename in filenames:
                # print(os.path.join(dirname, filename))
                path = os.path.join(dirname, filename)
                if path[path.rfind("."):].lower() == ".pdf":
                    results.append(path)

        return results

    @staticmethod
    def substring_search(file_data, sub_one, sub_two):
        """docstring"""
        ocrr_data = dict.fromkeys(file_data, np.zeros(2)))

        for path in file_data:
            subprocess.run(["pdf2txt.py", "-o", "output", path])

            with open("output", 'r') as fhand:
                if platform.system() == 'Windows':
                    file_name = path[path.rfind("\\"):path.rfind(".")+1]
                else:
                    file_name = path[path.rfind("/"):path.rfind(".")+1]

                if sub_one is not "":
                    if sub_one in file_name:
                        ocrr_data[path][0]+=1
                        ocrr_data[path][1]+=1

                    for line in 


                if sub_two is not "":
                    if sub_two in file_name:
                        ocrr_data[path][0]+=1
                        ocrr_data[path][1]+=1
