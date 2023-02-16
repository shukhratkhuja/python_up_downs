"""
Task Scheduler: 
A task scheduler is a class that manages the scheduling of tasks in an application. 
This scheduler can be implemented as a singleton to ensure that 
only one instance of the task scheduler is used by the application.
"""
import time

class TaskScheduler:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        self.tasks = []

    def schedule_task(self, task, delay):
        time.sleep(delay)
        task()

task_scheduler = TaskScheduler()
task_scheduler.schedule_task(lambda: print('Task 1'), 5)
another_task_scheduler = TaskScheduler()
another_task_scheduler.schedule_task(lambda: print('Task 2'), 10)
