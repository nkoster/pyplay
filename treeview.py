import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

people = [('Gijs', 66, 'Kunstenaar'),
          ('Henk', 22, 'Kok'),
          ('Freek', 50, 'Manager'),
          ('Petra', 47, 'Lerares'),
          ('Sjors', 31, 'Beveiliger')]

class MainWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="People")
        self.set_border_width(10)

        box = Gtk.Box()
        self.add(box)

        people_list_store = Gtk.ListStore(str, int, str)
        for item in people:
            people_list_store.append(list(item))

        for row in people_list_store:
            print(row[0])

        people_tree_view = Gtk.TreeView(people_list_store)

        for i, col_title in enumerate(['Name', 'Age', 'Profession']):
            # renderer = how render data
            renderer = Gtk.CellRendererText()
            # create columns - text = column nr
            column = Gtk.TreeViewColumn(col_title, renderer, text=i)

            # make colums sortable
            column.set_sort_column_id(i)

            people_tree_view.append_column(column)

        selected_row = people_tree_view.get_selection()
        selected_row.connect('changed', self.item_selected)

        box.pack_start(people_tree_view, True, True, 0)

    def item_selected(self, selection):
        model, row = selection.get_selected()
        if row is not None:
            print(model[row][0], model[row][1], model[row][2])


win = MainWindow()
win.connect('delete-event', Gtk.main_quit)
win.show_all()
Gtk.main()
