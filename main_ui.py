import customtkinter as ctk
import tkinter as tk

from tkinter import messagebox
from storage import load_tasks, save_tasks

class TodoApp:
    def __init__(self, root):

        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("500x450")
        self.root.resizable(False, False)
        self.root.configure(text_color = "#f0f4f7")

        self.tasks = load_tasks()
        self.setup_ui()
        self.refresh_listbox()
        
    def setup_ui(self):
        title_label = ctk.CTkLabel(
            self.root,
            text = "To-Do List",
            font = ("Helvetica", 22, "bold"),
            text_color = '#f0f4f7'
        )
        title_label.pack(pady=10)

        input_frame = ctk.CTkFrame(self.root)
        input_frame.pack(pady=10)

        self.task_entry = ctk.CTkEntry(
            input_frame,
            font = ("Helvetica", 12),
            width = 200,
            text_color = '#f0f4f7'
        )
        self.task_entry.pack(side="left", padx=(0, 10))

        add_button = ctk.CTkButton(
            input_frame,
            text = "Add Task",
            font = ("Helvetica", 11, "bold"),
            fg_color = "#27ae60",
            text_color = "white",
            command = self.add_task
        )
        add_button.pack(side="left", padx=10)

        list_frame = ctk.CTkFrame(self.root, fg_color="#f0f4f7")
        list_frame.pack(pady=10, fill = "both", expand=True)

        self.task_listbox = tk.Listbox(
            list_frame,
            font = ("Helvetica", 12),
            width = 45,
            height = 10,
            activestyle = "none",
            fg = '#000000'
        )
        self.task_listbox.pack(side="left", fill="both", expand=True)

        scrollbar = ctk.CTkScrollbar(list_frame)
        scrollbar.pack(side="right", fill="y")

        self.task_listbox.configure(yscrollcommand=scrollbar.set)
        scrollbar.configure(command=self.task_listbox.yview)

        self.info_label = ctk.CTkLabel(
            self.root,
            text = "",
            font = ("Helvetica", 11),
            text_color = "#f0f4f7"
        )              
        self.info_label.pack(pady=5)

        button_frame = ctk.CTkFrame(self.root)
        button_frame.pack(pady=10)

        mark_done_button = ctk.CTkButton(
            button_frame,
            text = "Mark as Done",
            font = ("Helvetica", 11, "bold"),
            fg_color = "#2980b9",
            text_color = "white",
            command=self.mark_done
        )     
        mark_done_button.pack(side="left", padx=5)

        delete_button = ctk.CTkButton(
            button_frame,
            text = "Delete Task",
            font = ("Helvetica", 11, "bold"),
            fg_color = "#c0392b",
            text_color = "white",
            command=self.delete_task
        ) 
        delete_button.pack(side="left", padx=5)

        clear_button = ctk.CTkButton(
            button_frame,
            text= "Clear All",
            font = ("Helvetica", 11, "bold"),
            fg_color = "#7f8c8d",
            text_color = "white",
            command=self.clear_all
        )
        clear_button.pack(side="left", padx=5)

    def refresh_listbox(self):
        self.task_listbox.delete(0, ctk.END)
        for index, task in enumerate(self.tasks, start=1):
            status = "✅" if task["done"] else "❌"
            display_text = f"{index}.{task['task']} [{status}]"
            self.task_listbox.insert(ctk.END, display_text)

    def add_task(self):

        task_text = self.task_entry.get().strip()
        if not task_text:
            self.info_label.configure(text = "Please enter a task first.")
            return
    
        self.tasks.append({"task" : task_text, "done" : False})
        save_tasks(self.tasks)
        self.task_entry.delete(0, ctk.END)
        self.info_label.configure(text = f"Task '{task_text}' added!")
        self.refresh_listbox()

    def get_selected_index(self):
        selection = self.task_listbox.curselection()
        if not selection:
            messagebox.showinfo("No Selection", "Please select a task first.")
            return None
        return selection[0]
    
    def mark_done(self):
        index = self.get_selected_index()
        if index is None:
            return
        
        self.tasks[index]["done"] = True
        save_tasks(self.tasks)
        self.info_label.configure(text = "Task marked as done!")
        self.refresh_listbox()

    def delete_task(self):
        index = self.get_selected_index()
        if index is None:
            return
        
        removed = self.tasks.pop(index)
        self.info_label.configure(text = f"Deleted task: {removed['task']}")
        save_tasks(self.tasks)
        self.refresh_listbox()

    def clear_all(self):
        if not self.tasks:
            self.info_label.configure(text = "No tasks to clear.")
            return
        
        if messagebox.askyesno("Clear all", "Are you sure you want to delete all tasks?"):
            self.tasks.clear()
            save_tasks(self.tasks)
            self.refresh_listbox()
            self.info_label.configure(text = "All tasks cleared!")

if __name__ == "__main__":
    root = ctk.CTk()
    app = TodoApp(root)
    root.mainloop()
