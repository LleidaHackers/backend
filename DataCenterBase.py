class DatacenterBase:
  id: int
  gridConnection: int
  waterConnection: int
  spaceX: int
  spaceY: int
  modules: list

  def __init__(self, gridConnection, waterConnection, spaceX, spaceY):
    self.gridConnection = gridConnection
    self.waterConnection = waterConnection
    self.spaceX = spaceX
    self.spaceY = spaceY
    self.modules = []