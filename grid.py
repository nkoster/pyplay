import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title='Grid Example')
        grid = Gtk.Grid()
        self.add(grid)
        b1 = Gtk.Button(label='button 1')
        b2 = Gtk.Button(label='button 2')
        b3 = Gtk.Button(label='button 3')
        b4 = Gtk.Button(label='button 4')
        b5 = Gtk.Button(label='button 5')
        b6 = Gtk.Button(label='button 6')
        grid.add(b1)
        grid.attach(b2, 1, 0, 2, 1)
        grid.attach_next_to(b3, b1, Gtk.PositionType.BOTTOM, 1, 2)
        grid.attach_next_to(b4, b2, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(b5, b4, Gtk.PositionType.BOTTOM, 1, 1)
        grid.attach_next_to(b6, b3, Gtk.PositionType.BOTTOM, 2, 1)

window = MainWindow()
window.connect('delete-event', Gtk.main_quit)
window.show_all()
Gtk.main()
