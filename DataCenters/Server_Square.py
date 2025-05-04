from DataCenterBase import DataCenterBase

class ServerSquare(DataCenterBase):
  def __init__(self, name, gridConnection, waterConnection, spaceX, spaceY):
    super().__init__(name, gridConnection, waterConnection, spaceX, spaceY)
    self.externalNetwork: int = 0    # maximize, "objective"
    self.dataStorage: int = 100      # min
    self.processing: int = 1000      # min 
    self.price: int = 1000000        # max
  