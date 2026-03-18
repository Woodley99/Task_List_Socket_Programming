import customtkinter as ctk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("500x450")
        self.root.resizable(False, False)

        self.tasks = []
        self.setup_ui()
        

    def setup_ui(self):
        title_label = ctk.CTkLabel(
            self.root,
            text = "To-Do List",
            font = ("Helvetica", 22, "bold"),
        )

    