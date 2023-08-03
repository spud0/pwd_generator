import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class MainWindow(Gtk.Window):
    # the constructor of the parent class 
    def __init__(self): 
        super().__init__(title = "Pwd Gen")

        self.button = Gtk.Button(label = "Test")
        self.button.connect("clicked" , self.button_clicked)
        self.add(self.button)


    def button_clicked(self, widget):
        print("One step closer to the password generator")

