class TaskList:
  def __init__(self, tasks):
    self.tasks = tasks
    self.index = 0

  def isDone(self):
    return self.index >= len(self.tasks)

  def next(self):
    task = self.tasks[self.index]
    self.index += 1
    return task
