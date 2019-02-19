import sys

from datapipeline.datapipeline import runDataAcquirementPipeline
from common.exceptions import raiseInvalidArgumentExceptionIfInvalidArgument
from common.arguments import printCommandExplanations, printNoArgumentsProvidedMessage
from common.arguments import __CAPTURE_DATA, __HELP, __TRAIN, __ROBOT, __CAM_TEST, __OPTIMIZE_HYPER, __CONFUSION
from common.videocapture import releaseCameraAndDestroyWindows
import common.util as util
from train.train import train
from robot.robot import startRobot
from robot.camtest import camtest
from test.confusion import confusion
from train.hyperparamoptimizer import hyperParameterOptimizer


options = {
  __CAPTURE_DATA: runDataAcquirementPipeline,
  __CONFUSION: confusion,
  __TRAIN: train,
  __OPTIMIZE_HYPER: hyperParameterOptimizer,
  __ROBOT: startRobot,
  __CAM_TEST: camtest,
  __HELP: printCommandExplanations
}

if __name__ == '__main__':
  if len(sys.argv) == 1:
    printNoArgumentsProvidedMessage()
  else:
    argumentParameterMap = util.getArgumentParameterMap(sys.argv)

    for argument in argumentParameterMap:
      raiseInvalidArgumentExceptionIfInvalidArgument(argument, options)
      util.callWithParameters(options[argument], argumentParameterMap[argument])
  
  releaseCameraAndDestroyWindows()
