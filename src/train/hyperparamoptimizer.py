from train.train import train
from model.hyperparams import HyperParams
from bayes_opt import BayesianOptimization
from bayes_opt.observer import JSONLogger
from bayes_opt.event import Events
from bayes_opt.util import load_logs

def hyperParameterOptimizer():
  def blackbox(c1Filters, c1KernelSize, c1Strides,
              c2Filters, c2KernelSize, c2Strides,
              c3Filters, c3KernelSize, c3Strides,
              fcc1Units, fcc2Units, dropout1, dropout2):
    hyperParams = HyperParams()

    hyperParams.c1Filters = int(round(c1Filters))
    hyperParams.c1KernelSize = int(round(c1KernelSize))
    hyperParams.c1Strides = int(round(c1Strides))

    hyperParams.c2Filters = int(round(c2Filters))
    hyperParams.c2KernelSize = int(round(c2KernelSize))
    hyperParams.c2Strides = int(round(c2Strides))

    hyperParams.c3Filters = int(round(c3Filters))
    hyperParams.c3KernelSize = int(round(c3KernelSize))
    hyperParams.c3Strides = int(round(c3Strides))

    hyperParams.fcc1Units = int(round(fcc1Units))
    hyperParams.fcc2Units = int(round(fcc2Units))

    hyperParams.dropout1 = round(dropout1, 2)
    hyperParams.dropout2 = round(dropout2, 2)

    checkpoint = train(200, None, hyperParams)
    return checkpoint.validationAccuracy

  bounds = {
    'c1Filters': (100, 128),
    'c1KernelSize': (2, 2),
    'c1Strides': (2, 2),

    'c2Filters': (64, 100),
    'c2KernelSize': (2, 2),
    'c2Strides': (2, 2),

    'c3Filters': (32, 64),
    'c3KernelSize': (2, 2),
    'c3Strides': (2, 2),

    'fcc1Units': (32, 150),
    'fcc2Units': (32, 150),

    'dropout1': (0.2, 0.5),
    'dropout2': (0.2, 0.5),
  }

  optimizer = BayesianOptimization(
      f=blackbox,
      pbounds=bounds,
      random_state=1,
  )

  
  logger = JSONLogger(path="./logs.json")
  optimizer.subscribe(Events.OPTMIZATION_STEP, logger)
  load_logs(optimizer, logs=["./oldlogs.json"])
  optimizer.maximize(
      init_points=2,
      n_iter=36,
  )

  print(optimizer.max)

