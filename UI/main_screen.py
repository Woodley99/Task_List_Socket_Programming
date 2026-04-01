import customtkinter as ctk
import tkinter as tk


class MainScreen(ctk.CTkFrame):
    def __init__(self, master, app):
        super().__init__(master)

        self.app = app
        self.grid(row=0, column=0, sticky="nsew")

        self.setup_ui()

    def setup_ui(self):

        #create row object
        row_frame = ctk.CTkFrame(self, fg_color="transparent")
        row_frame.pack(fill="x", pady=10)

        # 3 grids for spacing the labels
        row_frame.grid_columnconfigure(0, weight=1, uniform="header")
        row_frame.grid_columnconfigure(1, weight=1, uniform="header")
        row_frame.grid_columnconfigure(2, weight=1, uniform="header")

        # Title
        title_label = ctk.CTkLabel(
            row_frame,
            text="To-Do List",
            font=("Helvetica", 22, "bold"),
            text_color="#f0f4f7",
            fg_color="transparent"
        )
        title_label.grid(row=0, column=1) # in row

        #username display
        self.username_label = ctk.CTkLabel(
            row_frame,
            text=self.app.current_user if self.app.current_user else "",
            font=("helvetica", 12, "bold"),
            text_color="#f0f4f7",
            fg_color="transparent"
        )
        self.username_label.grid(row=0, column=2, sticky="e", padx=10) # in row

        # Input area
        input_frame = ctk.CTkFrame(self, fg_color="transparent")
        input_frame.pack(pady=10)

        self.task_entry = ctk.CTkEntry(
            input_frame,
            font=("Helvetica", 12),
            width=200,
            text_color="#f0f4f7",
            fg_color="transparent"
        )
        self.task_entry.pack(side="left", padx=(0, 10))

        add_button = ctk.CTkButton(
            input_frame,
            text="Add Task",
            font=("Helvetica", 11, "bold"),
            fg_color="#27ae60",
            text_color="white",
            command=self.app.task_manager.add_task
        )
        add_button.pack(side="left", padx=10)

        # Task list area
        list_frame = ctk.CTkFrame(self, fg_color="#f0f4f7")
        list_frame.pack(pady=10, fill="both", expand=True)

        self.task_listbox = tk.Listbox(
            list_frame,
            font=("Helvetica", 12),
            width=45,
            height=10,
            activestyle="none",
            fg="#000000"
        )
        self.task_listbox.pack(side="left", fill="both", expand=True)

        scrollbar = ctk.CTkScrollbar(list_frame)
        scrollbar.pack(side="right", fill="y")

        self.task_listbox.configure(yscrollcommand=scrollbar.set)
        scrollbar.configure(command=self.task_listbox.yview)

        # Bottom info label
        self.info_label = ctk.CTkLabel(
            self,
            text="",
            font=("Helvetica", 11),
            text_color="#f0f4f7"
        )
        self.info_label.pack(pady=5)

        # Action buttons
        button_frame = ctk.CTkFrame(self, fg_color="transparent")
        button_frame.pack(pady=10)

        mark_done_button = ctk.CTkButton(
            button_frame,
            text="Mark as Done",
            font=("Helvetica", 11, "bold"),
            fg_color="#2980b9",
            text_color="white",
            command=self.app.task_manager.mark_done
        )
        mark_done_button.pack(side="left", padx=5)

        delete_button = ctk.CTkButton(
            button_frame,
            text="Delete Task",
            font=("Helvetica", 11, "bold"),
            fg_color="#c0392b",
            text_color="white",
            command=self.app.task_manager.delete_task
        )
        delete_button.pack(side="left", padx=5)

        clear_button = ctk.CTkButton(
            button_frame,
            text="Clear All",
            font=("Helvetica", 11, "bold"),
            fg_color="#7f8c8d",
            text_color="white",
            command=self.app.task_manager.clear_all
        )
        clear_button.pack(side="left", padx=5)



    def update_user(self):
        self.username_label.configure(text=self.app.current_user)