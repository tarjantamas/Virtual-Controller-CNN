# Virtual Controller Using CNNs

## Dependencies
Python 3.5.0
`pip install opencv-python`
`pip install --upgrade tensorflow-gpu==1.8.0` OR `pip install --upgrade tensorflow==1.8.0`
`pip install keras`
`pip install pyautogui`
`pip install pywin32`
`pip install bayesian-optimization`

## Models

- smallwheelmodel (used for detecting gestures for 'left', 'right' and 'forward')
- smallpedalmodel (used for detecting gestures for 'pedaldown', 'pedalup', 'brake')

## Data aquirement

In order to capture data for one of the models, you have to set the correct data path and correct model.

In `src/datapipeline/datapipeline.py` modify the following import:

`from common.path import ??? as DATA_PATH` 

`??? = BRAKE_IMAGES_ROOT` for capturing data for the pedal model.
`??? = WHEEL_CONTROLER_IMAGES_ROOT` for capturing data for the wheel model.

You will also need to change the following import in the same file:

`from model.??? import CLASSES, CLASS_COUNT`

`??? = smallpedalmodel` for capturing data for the pedal model.
`??? = smallwheelmodel` for capturing data for the wheel model.

When you start capturing data a preview of your webcam will appear. You will be prompted for a number of seconds to prepare
for a given class. You should gesture with your hands for the class and after a short timeout the webcam will start capturing
for a number of seconds. After that it will prompt you to prepare for the next class and so on.

To start this process run

`python main.py --capturedata 60 10` the parameters 60 and 10 mean that you will have 10 seconds to prepare for the next class
and it will capture for 60 seconds per class.

## Training
In order to train one of the models, you have to set the correct data path and correct model.

For training the wheel model set the following constants in `src/common/path.py`

`TRAIN_DATA_PATH = WHEEL_CONTROLER_IMAGES_ROOT`
`VALIDATION_DATA_PATH = WHEEL_CONTROLER_VALIDATION_DATA_ROOT`
`TEST_DATA_PATH = WHEEL_CONTROLER_IMAGES_ROOT`

In `src/train/train.py` modify import smallwheelmodel:
`import model.smallwheelmodel as trainModel`

For training the pedal model set the following constants in `src/common/path.py`

`TRAIN_DATA_PATH = BRAKE_IMAGES_ROOT`
`VALIDATION_DATA_PATH = BRAKE_VALIDATION_DATA_ROOT`
`TEST_DATA_PATH = BRAKE_IMAGES_ROOT`

In `src/train/train.py` modify import smallpedalmodel:
`import model.smallpedalmodel as trainModel`

## Robot
After training the models, you can run the virtual controller on windows machines.

`python main.py --robot "Forza Horizon 4 (or some other window name)"`

References:
Bayesian optimization lib: https://github.com/fmfn/BayesianOptimization


