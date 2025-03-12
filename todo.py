class ToDoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)
        print(f"Task added: {task}")

    def view_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            print("Tasks:")
            for index, task in enumerate(self.tasks, start=1):
                print(f"{index}. {task}")

    def delete_task(self, task_index):
        if 0 <= task_index < len(self.tasks):
            removed_task = self.tasks.pop(task_index)
            print(f"Task removed: {removed_task}")
        else:
            print("Invalid task index.")
    def Mark_completed(self, task_index):
        if 0 <= task_index < len(self.tasks):
            if self.tasks[task_index]["completed"]:
                print(f"Task '{self.tasks[task_index]['task']}' is already completed.")
            else:
                self.tasks[task_index]["completed"] = True
                print(f"Task marked as completed: {self.tasks[task_index]['task']}")
        else:
            print("Invalid task index.")


