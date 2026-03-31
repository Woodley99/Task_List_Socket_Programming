import customtkinter as ctk


class SignInScreen(ctk.CTkFrame):
    def __init__(self, master, app):
        super().__init__(master)

        self.app = app
        self.grid(row=0, column=0, sticky="nsew")

        self.setup_ui()

    def setup_ui(self):
        # Title
        title = ctk.CTkLabel(
            self,
            text="Sign Up",
            font=("Helvetica", 22, "bold")
        )
        title.pack(pady=20)

        # Continue button
        continue_button = ctk.CTkButton(
            self,
            text="Continue",
            command=self.go_to_main
        )
        continue_button.pack(pady=10)

    def go_to_main(self):
        self.app.show_screen("main")
        self.app.refresh_listbox()