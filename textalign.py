import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class MainWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Text")
        self.set_border_width(10)

        hbox = Gtk.Box(spacing=20)
        hbox.set_homogeneous(False)

        vbox_left = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=20)
        vbox_left.set_homogeneous(False)

        vbox_right = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=20)
        vbox_right.set_homogeneous(False)

        hbox.pack_start(vbox_left, True, True, 0)
        hbox.pack_start(vbox_right, True, True, 0)

        label = Gtk.Label('this is a plain label')
        vbox_left.pack_start(label, True, True, 0)

        label = Gtk.Label()
        label.set_text('This is a left aligned text\noh wow more lines!')
        label.set_justify(Gtk.Justification.LEFT)
        vbox_left.pack_start(label, True, True, 0)

        label = Gtk.Label()
        label.set_text('This is a right aligned text\noh wow more lines!')
        label.set_justify(Gtk.Justification.RIGHT)
        vbox_left.pack_start(label, True, True, 0)

        label = Gtk.Label('Hi my name is Niels I Love ham - Hi my name is Niels I Love ham - Hi my name is Niels I Love ham - Hi my name is Niels I Love ham - Hi my name is Niels I Love ham - Hi my name is Niels I Love ham - Hi my name is Niels I Love ham')
        label.set_line_wrap(True)
        label.set_justify(Gtk.Justification.FILL)
        vbox_right.pack_start(label, True, True, 0)

        label = Gtk.Label()
        label.set_markup('aap <small>aap</small> <big>noot</big>\n'
                         '<b>bla bla</b> <i><b><big>You Rock!</big></b></i>\n'
                         '<a href="https://w3b.net">w3b.net</a>')

        vbox_right.pack_start(label, True, True, 0)

        self.add(hbox)



win = MainWindow()
win.connect('delete-event', Gtk.main_quit)
win.show_all()
Gtk.main()
