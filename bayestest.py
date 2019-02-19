def black_box_function(x):
  """Function with unknown internals we wish to maximize.

  This is just serving as an example, for all intents and
  purposes think of the internals of this function, i.e.: the process
  which generates its output values, as unknown.
  """ 
  return (3*x ** 3 - 15 * x ** 2 - 4 * x + 24)


from bayes_opt import BayesianOptimization

# Bounded region of parameter space
pbounds = {'x': (-1, 2)}

optimizer = BayesianOptimization(
    f=black_box_function,
    pbounds=pbounds,
    random_state=1,
)

optimizer.maximize(
    init_points=4,
    n_iter=10,
)

print(optimizer.max)