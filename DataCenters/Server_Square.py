from DataCenterBase import DataCenterBase

class ServerSquare(DataCenterBase):
  def __init__(self):
    super().__init__(gridConnection=3, waterConnection=1, spaceX=1000, spaceY=500)
    self.externalNetwork: int = 0    # maximize, "objective"
    self.dataStorage: int = 100      # min
    self.processing: int = 1000      # min 
    self.price: int = 1000000        # max
  
