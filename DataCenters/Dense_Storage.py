class DenseStorage:
  gridConnection: int = 0 # unlimited, start at 0 then grow
  waterConnection: int = 0 # unlimited, start at 0 then grow
  spaceX: int = 0         # minimize
  spaceY: int = 0         # minimize
  dataStorage : int = 0   # maximize
  price: int = 5000000    # max