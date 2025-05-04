from DataCenterBase import DataCenterBase
class DenseStorage(DataCenterBase):
  def __init__(self, name, gridConnection, waterConnection, spaceX, spaceY):
    super().__init__(name, gridConnection, waterConnection, spaceX, spaceY)
    self.dataStorage : int = 0   # maximize
    self.price: int = 5000000    # max