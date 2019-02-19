import cv2
import os

from datapipeline.task.imagenames import ImageNameManager


class ImageIO:
  def __init__(self, dataRoot, classNames):
    self.dataRoot = dataRoot
    self.classNames = classNames
    self.imageNameManager = ImageNameManager(dataRoot, classNames)

  def saveImage(self, className, image):
    dirPath = os.path.join(self.dataRoot, str(self.classNames.index(className)))
    
    imageName = self.imageNameManager.getNextImageNameForClass(className)

    filePath = os.path.join(dirPath, imageName)
    cv2.imwrite(filePath, image)
