import tkinter as tk

class Task(tk.Frame):
    def __init__(self, master=None, task="", is_completed=False, remove_command=None, **kwargs):
        super().__init__(master, **kwargs)
        self.task = tk.StringVar(value=task)
        self.is_completed = tk.BooleanVar(value=is_completed)
        self.remove_command = remove_command
        self.create_widgets()

    def create_widgets(self):
        self.task_checkbutton = tk.Checkbutton(self, textvariable=self.task, variable=self.is_completed)
        self.task_checkbutton.pack(side=tk.LEFT)
        self.remove_button = tk.Button(self, text="Удалить", command=self.remove_task)
        self.remove_button.pack(side=tk.RIGHT)

    def remove_task(self):
        if self.remove_command:
            self.remove_command(self)

class TaskList(tk.Frame):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.tasks = []

    def add_task(self, task_text, is_completed=False):
        task = Task(self, task=task_text, is_completed=is_completed, remove_command=self.remove_task)
        task.pack(anchor=tk.W)
        self.tasks.append(task)

    def remove_task(self, task):
        task.destroy()
        self.tasks.remove(task)

class TaskManagerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Менеджер задач")

        self.task_list_frame = TaskList(self)
        self.task_list_frame.pack(fill=tk.BOTH, expand=True)

        self.new_task_entry = tk.Entry(self)
        self.new_task_entry.pack(fill=tk.X)

        self.add_task_button = tk.Button(self, text="Добавить задачу", command=self.add_task)
        self.add_task_button.pack(fill=tk.X)

    def add_task(self):
        task_text = self.new_task_entry.get()
        if task_text:
            self.task_list_frame.add_task(task_text)
            self.new_task_entry.delete(0, tk.END)

if __name__ == "__main__":
    app = TaskManagerApp()
    app.mainloop()