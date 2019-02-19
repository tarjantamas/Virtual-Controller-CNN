from datapipeline.task.task import Task
from datapipeline.task.saveimagetask import SaveImageWithClassFromWebCamTask



def getTasks(timePerClass, timeBeforeClass, classes, dataPath):
  tasks = []

  for dataClass in classes:
    prepareTask = Task(timeBeforeClass, "Prepare for '" + dataClass + "'")
    captureTask = SaveImageWithClassFromWebCamTask(timePerClass, dataClass, dataPath, classes)
    tasks.extend([prepareTask, captureTask])

  return tasks
