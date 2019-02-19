def getArgumentParameterMap(argv):
  '''
  Maps arguments to their list of parameters.
  :param argv: list of arguments from the command line
  :return: a map which maps argument names to their parameters.
  If the program is run in the following way:
  python main.py --capturedata param1 param2 param3 --othercommand param1 param2
  the return value will be:
  {
    '--capturedata': ['param1', 'param2', 'param3']
    '--othercomand': ['param1', 'param2']
  }
  '''
  argumentParameterMap = {}
  i = 0
  while i < len(argv):
    arg = argv[i]
    
    j = i + 1
    if '--' in arg:
      params = []  
      while j < len(argv) and '--' not in argv[j]:
        params.append(argv[j])
        j += 1
      argumentParameterMap[arg] = params
    i = j
  return argumentParameterMap

def callWithParameters(function, params):
  function(*params)

def isHigherThan(s1, s2):
  '''
  If s1 and s2 are base N string representations of numbers then this function behaves as a comparator.
  :input s1: string to be compared
  :input s2: string to be compared
  :return: Returns True if s1's length is higher than s2's without scanning each character.
  Returns False if s1's length is lower than s2's without scanning each character.
  In other cases it compares the characters at each position of s1 and s2 until a position 'i' comes up
  where s1[i] > s2[i] at which point it returns True. Returns False if no such position comes up.
  '''
  if len(s1) > len(s2):
    return True
  if len(s1) < len(s2):
    return False
  for i, j in zip(s1, s2):
    if i > j:
      return True
  return False