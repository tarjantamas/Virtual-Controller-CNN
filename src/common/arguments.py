
__CAPTURE_DATA = "--capturedata"
__TRAIN = "--train"
__ROBOT = "--robot"
__OPTIMIZE_HYPER = "--optimize"
__CONFUSION = "--confusion"
__CAM_TEST = "--camtest"
__HELP = "--help"

__ARGUMENT_EXPLANATIONS = {
  __CONFUSION: "Calculates the confusion matrix for the current model.",
  __CAPTURE_DATA: "Starts the data aquirement tool. Webcam required. Optional params: [timePerClass, timeBeforeClass]",
  __TRAIN: "Starts training on available data. Optional params: [epochs, codedHyperParams]",
  __OPTIMIZE_HYPER: "Starts bayesian optimization on hyper parameters for the configured model.",
  __ROBOT: "Starts virtual controller. Weights need to be available. Optional params: [windowName, wheelParamsCoded, pedalParamsCoded]",
  __CAM_TEST: "Starts capturing from webcam. Optiona params: [enablePreprocessing]",
  __HELP: "Prints the available options."
}

def printCommandExplanations():
  print()
  print('--Argument explanations'.ljust(100, '-'))
  print()
  for arg in __ARGUMENT_EXPLANATIONS:
    print(arg.ljust(20) + __ARGUMENT_EXPLANATIONS[arg])
  print()

def printNoArgumentsProvidedMessage():
    print()
    print("--No arguments provided. You need to provide at least one argument".ljust(100, '-'))
    printCommandExplanations()