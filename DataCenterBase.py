class DataCenterBase:
  id: int
  gridConnection: int
  waterConnection: int
  spaceX: int
  spaceY: int
  connectedIn: list[str] # List of ids of connected modules
  connectedOut: list[str] # List of ids of connected modules

  def __init__(self, gridConnection, waterConnection, spaceX, spaceY):
    self.gridConnection = gridConnection
    self.waterConnection = waterConnection
    self.spaceX = spaceX
    self.spaceY = spaceY
    self.connectedIn = []
    self.connectedOut = []