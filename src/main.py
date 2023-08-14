import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from gui import MainWindow

if __name__ == '__main__': 
   m = MainWindow()
   m.connect("destroy", Gtk.main_quit)
   m.show_all()
   Gtk.main()


