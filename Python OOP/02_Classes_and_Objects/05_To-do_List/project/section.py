from task import Task
from os import linesep


class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks = list()

    def add_task(self, new_task: Task):
        if new_task.name in [x.name for x in self.tasks]:
            return f"Task is already in the section {self.name}"
        self.tasks.append(new_task)
        return f"Task {new_task.details()} is added to the section"

    def complete_task(self, task_name: str):
        for task in self.tasks:
            if task_name == task.name:
                task.completed = True
                return f"Completed task {task.name}"
        else:
            return f"Could not find task with the name {task_name}"

    def clean_section(self):
        tasks_removed = len([x for x in self.tasks if x.completed])
        self.tasks = [x for x in self.tasks if not x.completed]
        return f"Cleared {tasks_removed} tasks."

    def view_section(self):
        return f"Section {self.name}:{linesep}" + linesep.join([task.details for task in self.tasks])
