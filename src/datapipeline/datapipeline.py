import cv2
import os
from time import time

from datapipeline.task.aquiredatatasks import getTasks
from datapipeline.task.tasklist import TaskList
from common.videocapture import CAMERA

from model.smallpedalmodel import CLASSES, CLASS_COUNT
from common.path import TEST_DATA_PATH as DATA_PATH



def createRequiredMissingDirectories():
  for i in range(CLASS_COUNT):
    path = os.path.join(DATA_PATH, str(i))
    if not os.path.isdir(path):
      os.makedirs(path)

def runDataAcquirementPipeline(timePerClass='60', timeBeforeClass='10'):
  print("Images will be saved in the followind data path:")
  print(DATA_PATH)
  print("Capturing for classes:", CLASSES)
  input("Press enter to continue...")

  timePerClass, timeBeforeClass = int(timePerClass), int(timeBeforeClass)

  createRequiredMissingDirectories()

  taskList = TaskList(getTasks(timePerClass, timeBeforeClass, CLASSES, DATA_PATH))

  previousTime = time()

  task = taskList.next()

  while True: 
    if task.isDone():
      if taskList.isDone():
        break
      task = taskList.next()

    ret, frame = CAMERA.read()

    currentTime = time()
    ellapsedTime = currentTime - previousTime
    previousTime = currentTime
    task.runTask(ellapsedTime)

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)

    cv2.putText(frame, task.displayMessage + task.getStatusCaption(), \
      (52, 52), cv2.FONT_HERSHEY_TRIPLEX, 1.2, (0, 0, 0), 1, cv2.LINE_AA)
    cv2.putText(frame, task.displayMessage + task.getStatusCaption(), \
      (50, 50), cv2.FONT_HERSHEY_TRIPLEX, 1.2, (255, 255, 255), 1, cv2.LINE_AA)
    
    cv2.imshow('image', frame)
    cv2.waitKey(60)
