import os
from common.path import BRAKE_WEIGHTS_ROOT
from model.hyperparams import HyperParams


CLASSES = [
  "Forward", "Cruise", "Break"
]

CLASS_COUNT = len(CLASSES)

INPUT_WIDTH = 200
INPUT_HEIGHT = 200
INPUT_CHANNELS = 1
OUTPUT_LENGTH = CLASS_COUNT
BATCH_SIZE = 50

WEIGHTS_ROOT = BRAKE_WEIGHTS_ROOT
WEIGHTS_PATH = os.path.join(WEIGHTS_ROOT, "temp.hdf5")


def getModel(hyperParams = HyperParams(), performUserCheck=False):
  global WEIGHTS_PATH 
  WEIGHTS_PATH = os.path.join(BRAKE_WEIGHTS_ROOT, "smallpedalmodel_" + hyperParams.getHyperParamSetName() + ".hdf5")

  if performUserCheck:
    print("Using", __name__)
    input("Press enter to continue...")

  from keras.layers import Conv2D, Dense, MaxPool2D, Activation, Flatten, Reshape, BatchNormalization, Dropout
  from keras.initializers import VarianceScaling
  from keras.optimizers import Adam
  from keras import Sequential
  

  model = Sequential()

  model.add(Conv2D(
    filters=hyperParams.c1Filters,
    kernel_size=(hyperParams.c1KernelSize, hyperParams.c1KernelSize),
    strides=(hyperParams.c1Strides, hyperParams.c1Strides),
    kernel_initializer=VarianceScaling(),
    input_shape=(INPUT_WIDTH, INPUT_HEIGHT, INPUT_CHANNELS)
  ))
  model.add(BatchNormalization())
  model.add(Activation('relu'))
  model.add(MaxPool2D(
    pool_size=(2, 2),
    strides=(2, 2)
  ))

  model.add(Conv2D(
    filters=hyperParams.c2Filters,
    kernel_size=(hyperParams.c1KernelSize, hyperParams.c1KernelSize),
    strides=(hyperParams.c1Strides, hyperParams.c1Strides),
    kernel_initializer=VarianceScaling()
  ))
  model.add(BatchNormalization())
  model.add(Activation('relu'))

  model.add(MaxPool2D(
    pool_size=(2, 2),
    strides=(2, 2)
  ))

  model.add(Conv2D(
    filters=hyperParams.c3Filters,
    kernel_size=(hyperParams.c1KernelSize, hyperParams.c1KernelSize),
    strides=(hyperParams.c1Strides, hyperParams.c1Strides),
    kernel_initializer=VarianceScaling()
  ))
  model.add(BatchNormalization())
  model.add(Activation('relu'))

  model.add(Flatten())

  model.add(Dense(
    units=hyperParams.fcc1Units,
    kernel_initializer=VarianceScaling(),
  ))
  model.add(BatchNormalization())
  model.add(Activation('relu'))
  model.add(Dropout(hyperParams.dropout1))

  model.add(Dense(
    units=hyperParams.fcc2Units,
    kernel_initializer=VarianceScaling(),
  ))
  model.add(BatchNormalization())
  model.add(Activation('relu'))
  model.add(Dropout(hyperParams.dropout2))

  model.add(Dense(
    units=OUTPUT_LENGTH,
    activation='softmax',
    kernel_initializer=VarianceScaling(),
  ))
  model.compile(loss='categorical_crossentropy', optimizer=Adam(lr=0.001), metrics=['accuracy'])
  model.summary()
  return model


def saveModelWeights(model):
  if not os.path.isdir(BRAKE_WEIGHTS_ROOT):
    os.makedirs(BRAKE_WEIGHTS_ROOT)
  backupPath = WEIGHTS_PATH + '_backup'
  if os.path.isfile(backupPath):
    os.remove(backupPath)
  if os.path.isfile(WEIGHTS_PATH):
    os.rename(WEIGHTS_PATH, backupPath)
  model.save_weights(WEIGHTS_PATH)
    
def loadModelWeights(model):
  input('Trying to load weights for pedal model from: ' + WEIGHTS_PATH)
  if os.path.isfile(WEIGHTS_PATH):
    model.load_weights(WEIGHTS_PATH)