import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from GTK_App.main_window import MainWindow


window = MainWindow()

window.connect("delete-event", Gtk.main_quit)
window.show_all()
Gtk.main()
