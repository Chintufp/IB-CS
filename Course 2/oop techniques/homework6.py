class project:
    def __init__ (self, id:int):
        self.id = id
        self.tasks = []

    def __str__ (self):
        return f'Project {self.id} with {len(self.tasks)} tasks and {sum(len(task.workers) for task in self.tasks)} workers'

class task:
    def __init__ (self, name:str):
        self.name = name
        self.workers = []

class worker:
    def __init__ (self, name:str, employed:bool):
        self.name = name
        self.employed = employed

bob = worker('Bob', True)
jeff = worker('Jeff', False)

task1 = task('Raise funds')
task2 = task('Build a website')

task1.workers.append(bob)
task2.workers.append(jeff)

project1 = project(2345654)
project1.tasks.append(task1)
project1.tasks.append(task2)

print(project1)