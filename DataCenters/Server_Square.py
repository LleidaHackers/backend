from DataCenterBase import DataCenterBase

class ServerSquare(DataCenterBase):
  externalNetwork: int = 0    # maximize, "objective"
  dataStorage: int = 100      # min
  processing: int = 1000      # min 
  price: int = 1000000        # max

  def __init__(self, ):
    super().__init__(gridConnection=3, waterConnection=1, spaceX=1000, spaceY=500)
  
