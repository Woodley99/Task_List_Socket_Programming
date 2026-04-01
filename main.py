import customtkinter as ctk
from tkinter import messagebox

from storage import load_tasks
from task_manager import TaskManager
from UI.main_screen import MainScreen
from UI.sign_in_ui import SignInScreen
from UI.register_ui import RegisterScreen


class TodoApp:
    def __init__(self, root):
        """
        Initialize the TodoApp with the necessary window settings,
        task manager, and screen configurations.
        """
        # Window appearance settings
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")

        # Root window configurations
        self.current_user = None
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("500x450")
        self.root.resizable(False, False)

        # Task and task manager setup
        self.tasks = load_tasks()
        self.task_manager = TaskManager(self)

        # Grid configuration for layout
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        # Create and store screen frames
        self.screens = {}
        self.screens["register"] = RegisterScreen(self.root, self)
        self.screens["signin"] = SignInScreen(self.root, self)
        self.screens["main"] = MainScreen(self.root, self)

        # Show the sign-in screen first
        self.show_screen("signin")

    def show_screen(self, name):
        """
        Raise the appropriate screen based on the provided name.
        """
        self.screens[name].tkraise()

        if name =="main":
            self.screens["main"].update_user()


    def get_selected_index(self):
        """
        Get the index of the selected task from the task list.
        """
        selection = self.screens["main"].task_listbox.curselection()
        if not selection:
            messagebox.showinfo("No Selection", "Please select a task first.")
            return None
        return selection[0]

    def refresh_listbox(self):
        """
        Refresh the task listbox to reflect the current tasks.
        """
        main_screen = self.screens["main"]
        main_screen.task_listbox.delete(0, ctk.END)

        for index, task in enumerate(self.tasks, start=1):
            status = "✅" if task["done"] else "❌"
            display_text = f"{index}. {task['task']} [{status}]"
            main_screen.task_listbox.insert(ctk.END, display_text)


if __name__ == "__main__":
    root = ctk.CTk()
    app = TodoApp(root)
    root.mainloop()