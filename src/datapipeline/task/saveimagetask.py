from datapipeline.task.task import Task
from datapipeline.task.imageio import ImageIO
from common.videocapture import CAMERA



class SaveImageWithClassFromWebCamTask(Task):
  def __init__(self, durationSeconds, className, dataPath, classes):
    super().__init__(durationSeconds, "Capturing for '" + className + "'")
    self.className = className
    self.imageIO = ImageIO(dataPath, classes)

  def runTask(self, ellapsedTime):
    super().runTask(ellapsedTime)
    ret, frame = CAMERA.read()
    self.imageIO.saveImage(self.className, frame)
