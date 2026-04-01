import customtkinter as ctk

from user_storage import register_user_data

class RegisterScreen(ctk.CTkFrame):
    def __init__(self, master, app):
        super().__init__(master)

        self.app = app
        self.grid(row=0, column=0, sticky="nsew")

        self.setup_ui()

    def setup_ui(self):
        # Title
        title = ctk.CTkLabel(
            self,
            text="Register",
            font=("Helvetica", 22, "bold")
        )
        title.pack(pady=20)

        # username label
        username_label = ctk.CTkLabel(
            self,
            text = "Username"
        )
        username_label.pack()


        # username entry
        self.username_entry = ctk.CTkEntry(self)
        self.username_entry.pack(pady=5)

        # password label
        password_label = ctk.CTkLabel(
            self,
            text = "Password"
        )
        password_label.pack()

        # password entry
        self.password_entry = ctk.CTkEntry(
            self,
            show = "*"
        )
        self.password_entry.pack(pady=10)

        # password visiblity toggle
        self.toggle_button = ctk.CTkButton(
            self,
            text ="Show Password",
            command=self.toggle_password_visibility
            ) # default
        self.toggle_button.pack(pady=5)

        # message label
        self.message_label = ctk.CTkLabel(
            self,
            text= "",
            text_color = "red"
        )
        self.message_label.pack(pady = 5)

        row_frame = ctk.CTkFrame(self, fg_color="transparent")
        row_frame.pack(pady=10)


        # Sign in navigation button
        SignIn_nav_button = ctk.CTkButton(
            row_frame,
            text="Sign In?",
            command=self.SignIn_nav
        )
        SignIn_nav_button.pack(side="left", padx=10)

        # register button
        Register_button = ctk.CTkButton(
            row_frame,
            text="Register",
            command=self.register_user
        )
        Register_button.pack(side="left", padx=10)


        


    def toggle_password_visibility(self):
        # get the current state of the password entry(wether its shown or hidden)
        current_state = self.password_entry.cget("show")

        if current_state == "*": # if password is hidden
            self.password_entry.configure(show="") # show password
            self.toggle_button.configure(text="Hide Password")
        else: # if password visible
            self.password_entry.configure(show="*") # Hide password
            self.toggle_button.configure(text="Show Password")


    def register_user(self):

        username = self.username_entry.get().strip()
        password = self.password_entry.get().strip()

        # validate input
        if not username or not password:
            self.message_label.configure(text = "Enter username and password")
            return
        
        # call storage function
        success = register_user_data(username, password)

        if success:
            self.message_label.configure(text="Account created!", text_color="green")
        else:
            self.message_label.configure(text="User already exists")


    def SignIn_nav(self):
        self.app.show_screen("signin")