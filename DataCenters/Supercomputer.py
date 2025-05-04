from DataCenterBase import DataCenterBase

class Supercomputer(DataCenterBase):
  def __init__(self, gridConnection, waterConnection, spaceX, spaceY):  
    super().__init__(self, gridConnection, waterConnection, spaceX, spaceY)
    self.usablePower : int = 0     # minimize
    self.processing: int = 0       # maximize