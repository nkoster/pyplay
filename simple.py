import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MainWndow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Title")

window = MainWndow()
window.connect('delete-event', Gtk.main_quit)
window.show_all()
Gtk.main()
