from random import randint

class DatacenterBase:
  id: int
  gridConnection: int
  waterConnection: int
  spaceX: int
  spaceY: int
  modules: list

  def __init__(self, gridConnection, waterConnection, spaceX, spaceY):
    self.id = randint(1, 1000000)  # Random ID for the datacenter
    self.gridConnection = gridConnection
    self.waterConnection = waterConnection
    self.spaceX = spaceX
    self.spaceY = spaceY
    self.modules = []

  def addModule(self, module):
    if module in self.modules:
      raise ValueError("Module already exists in the datacenter.")
    self.modules.append(module)
  
  def removeModule(self, module):
    if module not in self.modules:
      raise ValueError("Module not found in the datacenter.")
    self.modules.remove(module)