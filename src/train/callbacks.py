from keras.callbacks import ModelCheckpoint, TensorBoard, ReduceLROnPlateau, Callback
import json
import os



lrReducer = ReduceLROnPlateau(monitor='val_loss', factor=0.9, patience=3, verbose=1)

class CustomCheckpoint(Callback):
  def __init__(self, model, trainModel):
    super().__init__()
    self.model = model
    self.saveWeightsFunction = trainModel.saveModelWeights
    self.loadWeightsFunction = trainModel.loadModelWeights
    self.validationAccuracy = 0
    
  def on_train_begin(self, logs={}, *args, **kwargs):
    self.loadWeightsFunction(self.model)
    return

  def on_train_end(self, logs={}, *args, **kwargs):
    self.saveWeightsFunction(self.model)
    return

  def on_epoch_begin(self, logs={}, *args, **kwargs):
    return

  def on_epoch_end(self, epoch, logs={}, *args, **kwargs):
    self.saveWeightsFunction(self.model)
    self.validationAccuracy = float(logs['val_acc'])
    with open("epoch.json", "a") as f:
      f.write(str(logs) + "\n")
    return

  def on_batch_begin(self, batch, logs={}, *args, **kwargs):
    return

  def on_batch_end(self, batch, logs={}, *args, **kwargs):
    return 
