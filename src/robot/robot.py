import pyautogui as R
import cv2
from win32gui import GetWindowText, GetForegroundWindow

from robot.keys import ROBOT_KEYS, KEYS, __CTYPE_KEYS, KEY_A, KEY_D, KEY_W, KEY_S, __ALL_KEYS
import model.smallwheelmodel as WM
import model.smallpedalmodel as PM
import preprocessor.wheelcontrollerpreprocessor as PP
from common.videocapture import CAMERA as cap
from robot.ctypeinterface import PressKey, ReleaseKey
from model.hyperparams import HyperParams
import numpy as np



def categoricalToKeyIndexLeftRight(y):
  keys = [KEY_A, None, KEY_D]
  return keys[np.argmax(y)]

def categoricalToKeyIndexForwardBackward(y):
  keys = [KEY_W, None, KEY_S]
  return keys[np.argmax(y)]

# pressKeyFunction = lambda i: R.keyDown(ROBOT_KEYS[i])
# releaseKeyFunction = lambda i: R.keyUp(ROBOT_KEYS[i])
# pressKeyFunction = lambda i: PressKey(__CTYPE_KEYS[i])
# releaseKeyFunction = lambda i: ReleaseKey(__CTYPE_KEYS[i])

keyStatus = [False for x in __ALL_KEYS]

def pressKeyFunction(index):
  if keyStatus[index] == False:
    keyStatus[index] = True
    PressKey(__CTYPE_KEYS[index])
  # else:
  #   releaseKeyFunction(index)

def releaseKeyFunction(index):
  if keyStatus[index] == True:
    keyStatus[index] = False
    ReleaseKey(__CTYPE_KEYS[index])

def isPressed(index):
  return keyStatus[index]


def startRobot(windowName=None, wheelParamsCoded=None, pedalParamsCoded=None):
  print("Robot is using the following models:")
  print("Wheel model:", WM.__name__)
  print("Pedal model:", PM.__name__)
  input("Press enter to continue...")

  import tensorflow as tf
  from keras.backend.tensorflow_backend import set_session
  
  config = tf.ConfigProto()
  config.gpu_options.allow_growth = True
  session = tf.Session(config=config)
  set_session(session)

  # wheelParams = HyperParams.parse(wheelParamsCoded)
  # pedalParams = HyperParams.parse(pedalParamsCoded)

  params = {"c1Filters": 128.0, "c2Filters": 64.0, "c3Filters": 64.0, "fcc1Units": 32.0, "fcc2Units": 32.0, "dropout1": 0.20000000238290275, "dropout2": 0.20000000094799325, "c1Strides": 2.0, "c2Strides": 2.0, "c3Strides": 2.0, "c1KernelSize": 2.0, "c2KernelSize": 2.0,  "c3KernelSize": 2.0}
  wheelParams = HyperParams(params)
  pedalParams = HyperParams(params)

  wheelModel = WM.getModel(wheelParams)
  WM.loadModelWeights(wheelModel)

  pedalModel = PM.getModel(pedalParams)
  PM.loadModelWeights(pedalModel)
  
  previousIndex = None
  
  if windowName is None:
    print("Provide a window name as an argument")
  print("Waiting for", windowName, "to be focused")

  started = False
  while True:
    currentWindowName = GetWindowText(GetForegroundWindow())
    isWindowFocused = currentWindowName == windowName

    if not isWindowFocused:
      print(currentWindowName)
    
    ret, frame = cap.read()
    cv2.imshow('image', frame)
    
    frame = cv2.resize(frame, dsize=(WM.INPUT_WIDTH, WM.INPUT_HEIGHT), interpolation=cv2.INTER_CUBIC)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame = frame.astype('float32') / 255.0
    frame = PP.process(frame)
    # cv2.imshow('processed', frame)

    cv2.waitKey(10)

    wheelResult = wheelModel.predict(frame.reshape((1, WM.INPUT_WIDTH, WM.INPUT_HEIGHT, WM.INPUT_CHANNELS)))
    brakeResult = pedalModel.predict(frame.reshape((1, PM.INPUT_WIDTH, PM.INPUT_HEIGHT, PM.INPUT_CHANNELS)))

    print(np.round(wheelResult), np.round(brakeResult))

    if not started:
      input("Robot ready, press enter to continue...")
      started = True

    wheelIndex = categoricalToKeyIndexLeftRight(wheelResult[0])
    brakeIndex = categoricalToKeyIndexForwardBackward(brakeResult[0])

    if isWindowFocused:      
      if KEY_A != wheelIndex:
        releaseKeyFunction(KEY_A)
      if KEY_D != wheelIndex:
        releaseKeyFunction(KEY_D)
      if KEY_W != brakeIndex:
        releaseKeyFunction(KEY_W)
      if KEY_S != brakeIndex:
        releaseKeyFunction(KEY_S)
      if wheelIndex is not None:
        pressKeyFunction(wheelIndex)
      if brakeIndex is not None:
        pressKeyFunction(brakeIndex)
      if brakeIndex is None:
        releaseKeyFunction(KEY_A)
        releaseKeyFunction(KEY_D)

    