class HyperParams:
  def __init__(self, params=None):
    if params is None:
      self.c1Filters = 128
      self.c1KernelSize = 2
      self.c1Strides = 2

      self.c2Filters = 64
      self.c2KernelSize = 2
      self.c2Strides = 2

      self.c3Filters = 32
      self.c3KernelSize = 2
      self.c3Strides = 2

      self.fcc1Units = 128
      self.fcc2Units = 64

      self.dropout1 = 0.4
      self.dropout2 = 0.4
    else:
      self.c1Filters = int(round(params['c1Filters']))
      self.c1KernelSize = int(round(params['c1KernelSize']))
      self.c1Strides = int(round(params['c1Strides']))

      self.c2Filters = int(round(params['c2Filters']))
      self.c2KernelSize = int(round(params['c2KernelSize']))
      self.c2Strides = int(round(params['c2Strides']))

      self.c3Filters = int(round(params['c3Filters']))
      self.c3KernelSize = int(round(params['c3KernelSize']))
      self.c3Strides = int(round(params['c3Strides']))

      self.fcc1Units = int(round(params['fcc1Units']))
      self.fcc2Units = int(round(params['fcc2Units']))

      self.dropout1 = round(params['dropout1'], 2)
      self.dropout2 = round(params['dropout2'], 2)
  
  @staticmethod
  def parse(string):
    tokens = string.split('-')

    hyperParams = HyperParams()
    hyperParams.c1Filters = int(tokens[0])
    hyperParams.c1KernelSize = int(tokens[1])
    hyperParams.c1Strides = int(tokens[2])

    hyperParams.c2Filters = int(tokens[3])
    hyperParams.c2KernelSize = int(tokens[4])
    hyperParams.c2Strides = int(tokens[5])

    hyperParams.c3Filters = int(tokens[6])
    hyperParams.c3KernelSize = int(tokens[7])
    hyperParams.c3Strides = int(tokens[8])

    hyperParams.fcc1Units = int(tokens[9])
    hyperParams.fcc2Units = int(tokens[10])

    hyperParams.dropout1 = float(tokens[11])
    hyperParams.dropout2 = float(tokens[12])

    return hyperParams

  def getHyperParamSetName(self):
    return '-'.join(map(lambda x: str(x), [
      self.c1Filters, self.c1KernelSize, self.c1Strides,
      self.c2Filters, self.c2KernelSize, self.c2Strides,
      self.c3Filters, self.c3KernelSize, self.c3Strides,
      self.fcc1Units,
      self.fcc2Units,
      self.dropout1,
      self.dropout2
    ]))