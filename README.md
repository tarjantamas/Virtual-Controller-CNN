# Virtual Controller Using CNNs

![usage example](http://37.59.67.242/html/softcomputing/example.gif)

## Dependencies
Python 3.5.0<br/>
`pip install opencv-python`<br/>
`pip install --upgrade tensorflow-gpu==1.8.0` OR `pip install --upgrade tensorflow==1.8.0`<br/>
`pip install keras`<br/>
`pip install pyautogui`<br/>
`pip install pywin32`<br/>
`pip install bayesian-optimization`<br/>

## Models

- smallwheelmodel (used for detecting gestures for 'left', 'right' and 'forward')
- smallpedalmodel (used for detecting gestures for 'pedaldown', 'pedalup', 'brake')

## Data acquirement

In order to capture data for one of the models, you have to set the correct data path and correct model.

In `src/datapipeline/datapipeline.py` modify the following import:

`from common.path import ??? as DATA_PATH`<br/> 

`??? = BRAKE_IMAGES_ROOT` for capturing data for the pedal model.<br/>
`??? = WHEEL_CONTROLER_IMAGES_ROOT` for capturing data for the wheel model.<br/>

You will also need to change the following import in the same file:

`from model.??? import CLASSES, CLASS_COUNT`

`??? = smallpedalmodel` for capturing data for the pedal model.<br/>
`??? = smallwheelmodel` for capturing data for the wheel model.<br/>

When you start capturing data a preview of your webcam will appear. You will be prompted for a number of seconds to prepare
for a given class. You should gesture with your hands for the class and after a short timeout the webcam will start capturing
for a number of seconds. After that it will prompt you to prepare for the next class and so on.

To start this process run

`python main.py --capturedata 60 10` the parameters 60 and 10 mean that you will have 10 seconds to prepare for the next class
and it will capture for 60 seconds per class.

## Training
In order to train one of the models, you have to set the correct data path and correct model.

For training the wheel model set the following constants in `src/common/path.py`

`TRAIN_DATA_PATH = WHEEL_CONTROLER_IMAGES_ROOT`<br/>
`VALIDATION_DATA_PATH = WHEEL_CONTROLER_VALIDATION_DATA_ROOT`<br/>
`TEST_DATA_PATH = WHEEL_CONTROLER_IMAGES_ROOT`<br/>

In `src/train/train.py` modify import smallwheelmodel:
`import model.smallwheelmodel as trainModel`

For training the pedal model set the following constants in `src/common/path.py`

`TRAIN_DATA_PATH = BRAKE_IMAGES_ROOT`<br/>
`VALIDATION_DATA_PATH = BRAKE_VALIDATION_DATA_ROOT`<br/>
`TEST_DATA_PATH = BRAKE_IMAGES_ROOT`<br/>

In `src/train/train.py` modify import smallpedalmodel:
`import model.smallpedalmodel as trainModel`

## Robot
After training the models, you can run the virtual controller on windows machines.

`python main.py --robot "Forza Horizon 4 (or some other window name)"`

References:
Bayesian optimization lib: https://github.com/fmfn/BayesianOptimization


