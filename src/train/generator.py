from keras.preprocessing.image import ImageDataGenerator
from common.path import TRAIN_DATA_PATH, VALIDATION_DATA_PATH, TEST_DATA_PATH
from preprocessor.wheelcontrollerpreprocessor import process



# print("Using these paths for training:")
# print("Train path:", TRAIN_DATA_PATH)
# print("Validation path:", VALIDATION_DATA_PATH)
# print("Test path:", TEST_DATA_PATH)
# input("Press enter to continue...")
class Generators:
  def __init__(self, model):
    self.trainDataGenerator = ImageDataGenerator(
      rescale=1./255,
      rotation_range=3,
      width_shift_range=0.01, 
      height_shift_range=0.01,
      brightness_range=[0.7, 1],
      zoom_range=[0.8, 1.2],
      preprocessing_function=process
    )

    self.validationDataGenerator = ImageDataGenerator(
      rescale=1./255,
      preprocessing_function=process    
    )

    self.testDataGenerator = ImageDataGenerator(
      rescale=1./255,
      preprocessing_function=process
    )

    self.trainGenerator = self.trainDataGenerator.flow_from_directory(
      TRAIN_DATA_PATH,
      target_size=(model.INPUT_WIDTH, model.INPUT_HEIGHT),
      batch_size=model.BATCH_SIZE,
      class_mode='categorical',
      color_mode='grayscale',
      # save_to_dir='./exampleimages'
    )

    self.validationGenerator = self.validationDataGenerator.flow_from_directory(
      VALIDATION_DATA_PATH,
      target_size=(model.INPUT_WIDTH, model.INPUT_HEIGHT),
      batch_size=model.BATCH_SIZE,
      class_mode='categorical',
      color_mode='grayscale',
      save_to_dir='./exampleimages'
    )

    self.testGenerator = self.testDataGenerator.flow_from_directory(
      TEST_DATA_PATH,
      target_size=(model.INPUT_WIDTH, model.INPUT_HEIGHT),
      batch_size=model.BATCH_SIZE,
      class_mode='categorical',
      color_mode='grayscale'
    )