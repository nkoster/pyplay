import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class MainWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Tabs Example")
        self.set_border_width(10)

        self.tabs = Gtk.Notebook()
        self.add(self.tabs)

        self.page1 = Gtk.Box()
        self.page1.set_border_width(10)
        self.page1.add(Gtk.Label('page 1'))
        self.tabs.append_page(self.page1, Gtk.Label('Tab One'))


win = MainWindow()
win.connect('delete-event', Gtk.main_quit)
win.show_all()
Gtk.main()
