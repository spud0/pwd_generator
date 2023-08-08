import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from passwd import generate_pwd, prefix_pwd_with_num, suffix_pwd_with_num

class MainWindow(Gtk.Window):
    # The constructor of the parent class 
    def __init__(self): 
        super().__init__(title = "Pwd Gen")
        self.set_default_size(600, 400)

        self.pwd = ""
        self.length = 0

        self.title = Gtk.Label()
        self.title.set_text("Password Generator")
        grid = Gtk.Grid()
        
        # Number of words in Password 
        self.num_words = Gtk.Entry()
        self.num_words.set_text("")

        # Field for the password
        self.password_display = Gtk.Entry()
        self.password_display.set_editable(False)

        # If the user input isn't a number, throw exception
        try:
            self.length = self.num_words.get_text() 

        except Exception as e: 
            self.num_words.set_text("Error: {}".format(e))
            self.num_words.set_editable(False)

        # Buttons for Password Generation and Modification
        self.generate_pwd_button = Gtk.Button(label = "Generate Password")
        self.generate_pwd_button.connect("clicked" , self.on_generate_pwd_button_clicked)
        # self.add(self.generate_pwd_button)

        # Prefix 
        self.prefix_pwd = Gtk.CheckButton(label = "Prefix Password With Number")
        self.prefix_pwd.connect("toggled", self.on_prefix_pwd_toggled)

        # Suffix
        self.suffix_pwd = Gtk.CheckButton(label = "Suffix Password With Number")
        self.suffix_pwd.connect("toggled", self.on_suffix_pwd_toggled)
        
        #Positions
        grid.attach(self.title, 0, 1, 3, 1)
        grid.attach(self.password_display, 1, 2, 3, 1)
        grid.attach(self.generate_pwd_button, 2, 3, 1, 1)
        grid.attach(self.prefix_pwd, 1, 4, 1, 1) 
        grid.attach(self.suffix_pwd, 4, 4, 1, 1)
        grid.attach(self.num_words, 2, 4, 1, 1) 

        self.add(grid)
    
        # Password Generator, and Modifiers
    def on_generate_pwd_button_clicked(self, widget):
        self.pwd = generate_pwd(self.length)
        self.password_display.set_text(self.pwd)

        if len(self.pwd) > 0: 
            self.num_words.set_editable(False)

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
