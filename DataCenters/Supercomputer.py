from DataCenterBase import DataCenterBase

class Supercomputer(DataCenterBase):
  def __init__(self):  
    super().__init__(self, gridConnection=0, waterConnection=0, spaceX=2000, spaceY=1000)
    self.usablePower : int = 0     # minimize
    self.processing: int = 0       # maximize