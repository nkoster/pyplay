import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk


class MainWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Input Example")
        self.set_border_width(10)

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
        self.add(vbox)

        self.username = Gtk.Entry()
        self.username.set_text('Username')
        vbox.pack_start(self.username, True, True, 0)

        self.password = Gtk.Entry()
        self.password.set_text('passssssswordyesyesyyes')
        self.password.set_visibility(False)
        vbox.pack_start(self.password, True, True, 0)

        self.button = Gtk.Button(label='Sign in')
        self.button.connect('clicked', self.sign_in)
        vbox.pack_start(self.button, True, True, 0)

    def sign_in(self, a):
        print(self.username.get_text(), self.password.get_text())


win = MainWindow()
win.connect('delete-event', Gtk.main_quit)
win.show_all()
Gtk.main()
