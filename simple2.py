import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, GObject

class Simple2(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Welcome to The Machine")

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)
        self.add(vbox)

        self.progressbar = Gtk.ProgressBar()
        vbox.pack_start(self.progressbar, True, True, 0)

        image = Gtk.Image.new_from_file('puffy.jpg')
        vbox.add(image)

        self.timeout_id = GObject.timeout_add(50, self.on_timeout, None)
        self.activity_mode = False

        self.label1 = Gtk.Label("This is a normal label")
        vbox.add(self.label1)

        button1 = Gtk.Button("Choose File")
        button1.connect("clicked", self.on_file_clicked)
        vbox.add(button1)
        
    def on_timeout(self, user_data):
        if self.activity_mode:
            self.progressbar.pulse()
        else:
            new_value = self.progressbar.get_fraction() + 0.01
            if new_value > 1:
                new_value = 0
            self.progressbar.pulse()
            #self.progressbar.set_fraction(new_value)
        return True

    def on_file_clicked(self, data):
        dialog = Gtk.FileChooserDialog("Please choose a file", self,
            Gtk.FileChooserAction.OPEN,
            (Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
             Gtk.STOCK_OPEN, Gtk.ResponseType.OK))
        self.add_filters(dialog)
        response = dialog.run()
        if response == Gtk.ResponseType.OK:
            print("Open clicked")
            print("File selected: " + dialog.get_filename())
            self.label1.set_text(dialog.get_filename())
        elif response == Gtk.ResponseType.CANCEL:
            print("Cancel clicked")
        dialog.destroy()

    def add_filters(self, dialog):
        filter_text = Gtk.FileFilter()
        filter_text.set_name("Text files")
        filter_text.add_mime_type("text/plain")
        dialog.add_filter(filter_text)
        filter_py = Gtk.FileFilter()
        filter_py.set_name("Python files")
        filter_py.add_mime_type("text/x-python")
        dialog.add_filter(filter_py)
        filter_any = Gtk.FileFilter()
        filter_any.set_name("Any files")
        filter_any.add_pattern("*")
        dialog.add_filter(filter_any)

win = Simple2()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()

