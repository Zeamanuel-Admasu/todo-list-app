class ToDoList:
    def __init__(self):
        """Initialize an empty task list."""
        self.tasks = []

    def add_task(self, task):
        """Adds a task to the list with a default status of not completed."""
        self.tasks.append({"task": task, "completed": False})  
        print(f"Task added: {task}")

    def view_tasks(self):
        """Displays all tasks with their completion status."""
        if not self.tasks:
            print("No tasks in the list.")
        else:
            print("Tasks:")
            for index, task in enumerate(self.tasks, start=1):
                status = "✓" if task["completed"] else "✗"
                print(f"{index}. {task['task']} [{status}]")

    def delete_task(self, task_index):
        """Removes a task by index if valid, otherwise raises an IndexError."""
        if 0 <= task_index < len(self.tasks):
            removed_task = self.tasks.pop(task_index)
            print(f"Task removed: {removed_task['task']}")
        else:
            raise IndexError("Invalid task index.")  

    def mark_completed(self, task_index):
        """Marks a task as completed if it exists and isn't already completed."""
        if 0 <= task_index < len(self.tasks):
            if self.tasks[task_index]["completed"]:
                print(f"Task '{self.tasks[task_index]['task']}' is already completed.")
            else:
                self.tasks[task_index]["completed"] = True
                print(f"Task marked as completed: {self.tasks[task_index]['task']}")
        else:
            raise IndexError("Invalid task index.")  


