import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class MainWindow(Gtk.Window):
    """docstring for MainWindow."""
    def __init__(self):
        super(MainWindow, self).__init__(title="myapp")
        self.set_border_width(10)
        self.set_default_size(500, 300)

        # Vbox
        self.base_layout = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=8)
        self.add(self.base_layout)

        # VBox row one
        self.row_one = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

        # Row_one's Label_one
        self.label_one = Gtk.Label()
        self.label_one.set_label("Search String:")
        self.row_one.pack_start(self.label_one, False, True, 0)

        # Entry one
        self.entry_one = Gtk.Entry()
        self.row_one.pack_start(self.entry_one, False, True, 0)

        # Row_one's Search Button
        self.s_btn = Gtk.Button(label="search")
        self.s_btn.connect("clicked", self.run_search)
        self.row_one.pack_start(self.s_btn, False, True, 1)

        self.base_layout.pack_start(self.row_one, False, True, 0)

        # Vmox row two
        self.row_two = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=0)
        self.base_layout.pack_start(self.row_two, True, True, 0)


    def run_search(self, widget):
        print("danb")

    def show_serach_results(slef, data):
        """
        :param data: List of tuples
        """
        data_list_store = Gtk.ListStore(str, int)
        for item in data:
            data_list_store.append(list(item))

        data_tree_view = Gtk.TreeView(data_list_store)

        for i, col_title in enumerate(["File/Directory", "Ocurrences"]):

            rederer = Gtk.CellRendererText()
            column = Gtk.TreeViewColumn(col_title, renderer, text=i)
            data_tree_view.append_collumn(column)

        self.row_two.pack_start(data_tree_view, True, True, 0)
        pass
