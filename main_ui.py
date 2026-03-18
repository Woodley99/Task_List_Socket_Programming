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

        input_frame = ctk.Frame(self.root, bg = "#f0f4f7")
        input_frame.pack(pad=10)

        self.task_entry = ctk.Entry(
            input_frame,
            font = ("Helvetica", 12),
            width = 30
        )
        self.task_entry.pack(side="left", padx=(0, 20))

        add_button = ctk.Button(
            input_frame,
            text = "Add Task",
            font = ("Helvetica", 11, "bold"),
            bg = "#27ae60",
            fg = "white",
            padx = 10,
            command = self.add_task
        )
        add_button.pack(side="left")

        list_frame = ctk.Frame(self.root, bg="#f0f4f7")
        list_frame.pack(pady=10, fill = "both", expand=True)

        self.task_listbox = ctk.Listbox(
            list_frame,
            font = ("Helvetica", 12),
            width = 45,
            height = 10,
            activestyle = "none"
        )
        self.task_listbox.pack(side="left", fill="both", expand=True)

        scrollbar = ctk.Scrollbar(list_frame)
        scrollbar.pack(side="right", fill="y")

        self.task_listbox.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.task_listbox.yview)

        self.info_label = ctk.Label(
            self.root,
            text = "",
            font = ("Helvetica", 11),
            bg = "#f0f4f7",
            fg = "#007acc"
        )              
        self.info_label.pack(pady=5)

        button_frame = ctk.Frame(self.root, bg = "#f0f4f7")
        button_frame.pack(pady=10)

        mark_done_button = ctk.Button(
            button_frame,
            text = "Mark as Done",
            font = ("Helvetica", 11, "bold"),
            bg = "#2980b9",
            fg = "white",
            padx = 10,
            command=self.mark_done
        )     
        mark_done_button.pack(side="left", padx=5)

        delete_button = ctk.Button(
            button_frame,
            text = "Delete Task",
            font = ("Helvetica", 11, "bold"),
            bg = "#c0392b",
            fg = "white",
            padx=10,
            command=self.delete_task
        ) 
        delete_button.pack(side="left", padx=5)

        clear_button = ctk.Button(
            button_frame,
            text= "Clear All",
            font = ("Helvetica", 11, "bold"),
            bg = "#7f8c8d",
            fg = "white",
            padx=10,
            command=self.clear_all
        )
        clear_button.pack(side="left", padx=5)

    def refresh_listbox(self):
        self.task_listbox.delete(0, ctk.End)
        for index, task in enumerate(self.tasks, start=1):
            status = "✅" if task["done"] else "❌"
            display_text = f"{index}.{task['task']} [{status}]"
            self.tasl_listbox.insert(ctk.END, display_text)
