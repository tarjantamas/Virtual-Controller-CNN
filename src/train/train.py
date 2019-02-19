def train(epochs='20', codedHyperParams=None, *hyperParams):
  from train.callbacks import CustomCheckpoint, lrReducer
  from train.generator import Generators
  import model.smallwheelmodel as trainModel
  from model.hyperparams import HyperParams

  if codedHyperParams is not None:
    hyperParams = (HyperParams.parse(codedHyperParams),)

  params = {"c1Filters": 128.0, "c2Filters": 64.0, "c3Filters": 64.0, "fcc1Units": 32.0, "fcc2Units": 32.0, "dropout1": 0.20000000238290275, "dropout2": 0.20000000094799325, "c1Strides": 2.0, "c2Strides": 2.0, "c3Strides": 2.0, "c1KernelSize": 2.0, "c2KernelSize": 2.0,  "c3KernelSize": 2.0}
  hyperParams = (HyperParams(params),)

  epochs = int(epochs)

  generators = Generators(trainModel)
  model = trainModel.getModel(*hyperParams)
  checkpoint = CustomCheckpoint(model, trainModel)
  model.fit_generator(
    generators.trainGenerator,
    steps_per_epoch=50,
    epochs=epochs,
    validation_data=generators.validationGenerator,
    validation_steps=50,
    callbacks=[checkpoint, lrReducer]
  )

  return checkpoint
