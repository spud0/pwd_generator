import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from passwd import generate_pwd, prefix_pwd_with_num, suffix_pwd_with_num, remove_nums

class MainWindow(Gtk.Window):
    # The constructor of the parent class 
    def __init__(self): 
        super().__init__(title = "Psuedo-Random Password Generator")
        self.set_default_size(600, 400)

        self.pwd = ""
        self.length = 0

        self.title = Gtk.Label()
        self.title.set_text("Password Output")
        self.title.set_hexpand(True)

        self.pwd_length_label = Gtk.Label()
        self.pwd_length_label.set_text("Number of words in Password")
        self.pwd_length_label.set_hexpand(True)

        # Containers 
        grid = Gtk.Grid()
        
        # Number of words in Password 
        self.num_words = Gtk.Entry()
        self.num_words.set_text("")
        self.num_words.set_editable(True)
        self.num_words.set_max_length(1)

        # Text field for the password
        self.pwd_display = Gtk.Entry()
        self.pwd_display.set_editable(False)
         
        # Buttons for Password Generation and Modification
        self.generate_pwd_button = Gtk.Button(label = "Generate Password")
        self.generate_pwd_button.connect("clicked" , self.on_generate_pwd_button_clicked)
        self.generate_pwd_button.set_border_width(10)

        # Prefix 
        self.prefix_pwd = Gtk.CheckButton(label = "Prefix Password With Number")
        self.prefix_pwd.connect("toggled", self.on_prefix_pwd_toggled)
        self.prefix_pwd.set_border_width(10)

        # Suffix
        self.suffix_pwd = Gtk.CheckButton(label = "Suffix Password With Number")
        self.suffix_pwd.connect("toggled", self.on_suffix_pwd_toggled)
        self.suffix_pwd.set_border_width(10)
 
        # Positions
        grid.set_border_width(3)
        grid.attach(self.title, 2, 1, 1, 1)
        grid.attach(self.pwd_display, 1, 2, 4, 1)
        grid.attach(self.generate_pwd_button, 2, 3, 1, 1)
        grid.attach(self.prefix_pwd, 1, 7, 1, 1) 
        grid.attach(self.suffix_pwd, 4, 7, 1, 1)
        grid.attach(self.pwd_length_label, 2, 6, 1, 1)
        grid.attach(self.num_words,  2, 7, 1, 1) 
        self.add(grid)
    
        
    def on_generate_pwd_button_clicked(self, widget):

        self.length = self.num_words.get_text()
        
        try: 
            self.length = int(self.length)
            self.pwd = generate_pwd(self.length)
            self.pwd_display.set_text(self.pwd) 
        except ValueError: 
            error_msg = "Error: Non Number Input, Invalid Type Integer."
            self.pwd_display.set_text(error_msg)
        
    def on_prefix_pwd_toggled(self, button):
        if button.get_active():
            self.pwd = prefix_pwd_with_num(self.pwd)
            self.pwd_display.set_text(self.pwd)
        
        else:
            self.pwd = remove_nums(self.pwd)
            self.pwd_display.set_text(self.pwd)

    def on_suffix_pwd_toggled(self, button):
        if button.get_active():
            self.pwd = suffix_pwd_with_num(self.pwd)
            self.pwd_display.set_text(self.pwd)

        else: 
            self.pwd = remove_nums(self.pwd)
            self.pwd_display.set_text(self.pwd)


m = MainWindow()
m.connect("destroy", Gtk.main_quit)
m.show_all()
Gtk.main()
