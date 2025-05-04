from DataCenterBase import DataCenterBase
class DenseStorage(DataCenterBase):
  def __init__(self):
    super().__init__(gridConnection=0, waterConnection=0, spaceX=0, spaceY=0)
    self.dataStorage : int = 0   # maximize
    self.price: int = 5000000    # max