import customtkinter as ctk
from tkinter import messagebox
from storage import save_tasks


class TaskManager:
    def __init__(self, app):
        self.app = app

    def add_task(self):
        main_screen = self.app.screens["main"]

        task_text = main_screen.task_entry.get().strip()
        if not task_text:
            main_screen.info_label.configure(text="Please enter a task first.")
            return

        self.app.tasks.append({"task": task_text, "done": False})
        save_tasks(self.app.tasks)

        main_screen.task_entry.delete(0, ctk.END)
        main_screen.info_label.configure(text=f"Task '{task_text}' added!")

        self.app.refresh_listbox()

    def mark_done(self):
        main_screen = self.app.screens["main"]

        index = self.app.get_selected_index()
        if index is None:
            return

        self.app.tasks[index]["done"] = True
        save_tasks(self.app.tasks)

        main_screen.info_label.configure(text="Task marked as done!")
        self.app.refresh_listbox()

    def delete_task(self):
        main_screen = self.app.screens["main"]

        index = self.app.get_selected_index()
        if index is None:
            return

        removed = self.app.tasks.pop(index)
        save_tasks(self.app.tasks)

        main_screen.info_label.configure(text=f"Deleted task: {removed['task']}")
        self.app.refresh_listbox()

    def clear_all(self):
        main_screen = self.app.screens["main"]

        if not self.app.tasks:
            main_screen.info_label.configure(text="No tasks to clear.")
            return

        if messagebox.askyesno("Clear all", "Are you sure you want to delete all tasks?"):
            self.app.tasks.clear()
            save_tasks(self.app.tasks)

            main_screen.info_label.configure(text="All tasks cleared!")
            self.app.refresh_listbox()