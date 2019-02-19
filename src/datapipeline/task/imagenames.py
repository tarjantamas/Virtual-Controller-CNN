import os
import common.util as util



class ImageNameManager:
  def __init__(self, root, classNames):
    self.lastImageNameForClass = self.__findLastImageNameForEachClass(root, classNames)
    
  def __findLastImageNameForEachClass(self, root, classNames):
    result = {}
    for className, index in zip(classNames, range(len(classNames))):
      result[className] = self.__getMaxImageNameInDirectory(os.path.join(root, str(index)))
    return result

  def __getMaxImageNameInDirectory(self, path):
    files = os.listdir(path)
    maxName = '0.jpg'
    for fileName in files:
      if util.isHigherThan(fileName, maxName):
        maxName = fileName
    return int(maxName.split('.')[0])

  def getNextImageNameForClass(self, className):
    self.lastImageNameForClass[className] += 1
    return str(self.lastImageNameForClass[className]) + '.jpg'