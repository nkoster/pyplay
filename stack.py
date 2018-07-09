import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MainWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Main Window")
        self.set_border_width(10)

        box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
        self.add(box)

        main_area = Gtk.Stack()
        main_area.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
        main_area.set_transition_duration(2000)

        check = Gtk.CheckButton("Don't check me")
        main_area.add_titled(check, 'check_name', 'Check Box')

        label = Gtk.Label()
        label.set_markup("<big>a big label</big>")
        main_area.add_titled(label, 'label_name', 'Label Tab')

        stack_switcher = Gtk.StackSwitcher()
        stack_switcher.set_stack(main_area)
        box.pack_start(stack_switcher, True, True, 0)
        box.pack_start(main_area, True, True, 0)

win = MainWindow()
win.connect('delete-event', Gtk.main_quit)
win.show_all()
Gtk.main()
