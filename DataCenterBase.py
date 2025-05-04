class DataCenterBase:
  id: int
  name: str
  gridConnection: int
  waterConnection: int
  spaceX: int
  spaceY: int
  connectedIn: list[str] # List of ids of connected modules
  connectedOut: list[str] # List of ids of connected modules

  def __init__(self, name, gridConnection, waterConnection, spaceX, spaceY):
    self.name = name
    self.gridConnection = gridConnection
    self.waterConnection = waterConnection
    self.spaceX = spaceX
    self.spaceY = spaceY
    self.connectedIn = [] # List of ids of connected modules
    self.connectedOut = []