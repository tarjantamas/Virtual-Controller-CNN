def confusion():
  from train.generator import Generators
  import tensorflow as tf
  import numpy as np

  import model.smallpedalmodel as testModel
  from model.hyperparams import HyperParams

  params = {"c1Filters": 128.0, "c2Filters": 64.0, "c3Filters": 64.0, "fcc1Units": 32.0, "fcc2Units": 32.0, "dropout1": 0.20000000238290275, "dropout2": 0.20000000094799325, "c1Strides": 2.0, "c2Strides": 2.0, "c3Strides": 2.0, "c1KernelSize": 2.0, "c2KernelSize": 2.0,  "c3KernelSize": 2.0}
  hyperParams = HyperParams(params)

  model = testModel.getModel(hyperParams)
  testModel.loadModelWeights(model)
  
  model.summary()

  batch_count = 200

  labels, predictions = [], []

  generators = Generators(testModel)

  for i in range(batch_count):
    for x, y in generators.testGenerator:
      pred = model.predict_classes(x)
      y = np.argmax(y, axis=1)

      for y1 in y:
        labels.append(y1)

      for y1 in pred:
        predictions.append(y1)
          
      break



  matrix = tf.confusion_matrix(labels, predictions)
  a, b = tf.metrics.mean_per_class_accuracy(tf.convert_to_tensor(labels), tf.convert_to_tensor(predictions), 3)

  sess = tf.Session()
  sess.as_default()
  sess.run(tf.global_variables_initializer())
  sess.run(tf.local_variables_initializer())
  print("Confusion matrix")
  print(sess.run(matrix))
  print(sess.run(a))
  print("Mean per class accuracy")
  print(sess.run(b))