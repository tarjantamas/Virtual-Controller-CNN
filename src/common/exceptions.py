def raiseInvalidArgumentException(arg):
  raise Exception('Invalid argument: ' + arg)

def raiseInvalidArgumentExceptionIfInvalidArgument(arg, options):
  if arg not in options:
    raiseInvalidArgumentException(arg)