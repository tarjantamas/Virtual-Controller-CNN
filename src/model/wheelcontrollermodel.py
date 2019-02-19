import os
from common.path import WHEEL_CONTROLER_WEIGHTS_ROOT



CLASSES = [
  "Left", "Forward", "Right"
]

CLASS_COUNT = len(CLASSES)

INPUT_WIDTH = 200
INPUT_HEIGHT = 200
INPUT_CHANNELS = 1
OUTPUT_LENGTH = CLASS_COUNT
BATCH_SIZE = 50

WEIGHTS_ROOT = WHEEL_CONTROLER_WEIGHTS_ROOT
WEIGHTS_PATH = os.path.join(WEIGHTS_ROOT, "weights.hdf5")

def getModel():
  print("Using", __name__)
  input("Press enter to continue...")

  from keras.layers import Conv2D, Dense, MaxPool2D, Activation, Flatten, Reshape, BatchNormalization, Dropout
  from keras.initializers import VarianceScaling
  from keras.optimizers import Adam
  from keras import Sequential

  model = Sequential()

  model.add(Conv2D(
    filters=32,
    kernel_size=(5, 5),
    strides=(5, 5),
    kernel_initializer=VarianceScaling(),
    input_shape=(INPUT_WIDTH, INPUT_HEIGHT, INPUT_CHANNELS)
  ))
  
  model.add(Activation('relu'))

  model.add(Conv2D(
    filters=64,
    kernel_size=(2, 2),
    kernel_initializer=VarianceScaling()
  ))
  
  model.add(Activation('relu'))

  model.add(MaxPool2D(
    pool_size=(2, 2),
    strides=(2, 2)
  ))

  model.add(Conv2D(
    filters=128,
    kernel_size=(2, 2),
    strides=(2, 2),
    kernel_initializer=VarianceScaling()
  ))
  
  model.add(Activation('relu'))

  model.add(Conv2D(
    filters=256,
    kernel_size=(2, 2),
    strides=(2, 2),
    kernel_initializer=VarianceScaling()
  ))
  
  model.add(Activation('relu'))

  model.add(Flatten())

  model.add(Dense(
    units=256,
    activation='relu',
    kernel_initializer=VarianceScaling(),
  ))

  model.add(Dropout(0.3))

  model.add(Dense(
    units=128,
    activation='relu',
    kernel_initializer=VarianceScaling(),
  ))

  model.add(Dropout(0.3))

  model.add(Dense(
    units=64,
    activation='relu',
    kernel_initializer=VarianceScaling(),
  ))

  model.add(Dropout(0.3))

  model.add(Dense(
    units=OUTPUT_LENGTH,
    activation='softmax',
    kernel_initializer=VarianceScaling(),
  ))
  model.compile(loss='categorical_crossentropy', optimizer=Adam(lr=0.00001), metrics=['accuracy'])
  model.summary()
  return model


def saveModelWeights(model):
  if not os.path.isdir(WHEEL_CONTROLER_WEIGHTS_ROOT):
    os.makedirs(WHEEL_CONTROLER_WEIGHTS_ROOT)
  backupPath = WEIGHTS_PATH + '_backup'
  if os.path.isfile(backupPath):
    os.remove(backupPath)
  if os.path.isfile(WEIGHTS_PATH):
    os.rename(WEIGHTS_PATH, backupPath)
  model.save_weights(WEIGHTS_PATH)
    
def loadModelWeights(model):
  if os.path.isfile(WEIGHTS_PATH):
    print('Loading weights')
    model.load_weights(WEIGHTS_PATH)