import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="List Box")
        self.set_border_width(10)
        listbox = Gtk.ListBox()
        listbox.set_selection_mode(Gtk.SelectionMode.NONE)
        self.add(listbox)
        
        row_1 = Gtk.ListBoxRow()
        box_1 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=40)
        row_1.add(box_1)
        label = Gtk.Label('Hello hello, pls check...')
        check = Gtk.CheckButton()
        box_1.pack_start(label, True, True, 0)
        box_1.pack_start(check, True, True, 0)
        listbox.add(row_1)
        
        row_2 = Gtk.ListBoxRow()
        box_2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=40)
        row_2.add(box_2)
        label = Gtk.Label('Hello hello, pls switch...')
        switch = Gtk.Switch()
        box_2.pack_start(label, True, True, 0)
        box_2.pack_start(switch, True, True, 0)
        listbox.add(row_2)

win = MainWindow()
win.connect('delete-event', Gtk.main_quit)
win.show_all()
Gtk.main()
