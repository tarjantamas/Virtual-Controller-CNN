import math

class Task:
  def __init__(self, durationSeconds, displayMessage, task=None):
    self.durationSeconds = durationSeconds
    self.currentDuration = 0
    self.displayMessage = displayMessage
  
  def isDone(self):
    return self.currentDuration >= self.durationSeconds
  
  def runTask(self, ellapsedTime):
    self.currentDuration += ellapsedTime

  def getStatusCaption(self):
    return "(" + str(max(math.floor(self.durationSeconds - self.currentDuration) + 1, 0)) + ")"