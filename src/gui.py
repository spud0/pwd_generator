import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from passwd import generate_pwd, prefix_pwd_with_num, suffix_pwd_with_num

class MainWindow(Gtk.Window):
    # The constructor of the parent class 
    def __init__(self): 
        super().__init__(title = "Pwd Gen")
        self.set_default_size(600, 400)

        # The Password
        self.pwd = ""

        # Layout of the Window
        grid = Gtk.Grid()


        # Number of words in Password 
        self.num_words = Gtk.Entry()
        self.num_words.set_text("Enter the Number of Words")

        # Buttons for Password Generation and Modification
        self.generate_pwd_button = Gtk.Button(label = "Generate Password")
        self.generate_pwd_button.connect("clicked" , self.on_generate_pwd_button_clicked)
        self.add(self.generate_pwd_button)

        # Prefix 
        self.prefix_pwd = Gtk.CheckButton(label = "Prefix Password With Number")
        self.prefix_pwd.connect("toggled", self.on_prefix_pwd_toggled)

        # Suffix
        self.suffix_pwd = Gtk.CheckButton(label = "Suffix Password With Number")
        self.suffix_pwd.connect("toggled", self.on_suffix_pwd_toggled)
        

        # Password Generator, and Modifiers
    def on_generate_pwd_button_clicked(self, widget):
        self.pwd = generate_pwd(self.num_words)

    def on_prefix_pwd_toggled(self, button):
        if button.get_active():
            self.pwd = prefix_pwd_with_num(self.pwd)

    def on_suffix_pwd_toggled(self, button):
        if button.get_active():
            self.pwd = suffix_pwd_with_num(self.pwd)



m = MainWindow()
m.connect("destroy", Gtk.main_quit)
m.show_all()
Gtk.main()
