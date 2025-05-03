class DataRackBase:
  # Position, may vary
  posX: int
  posY: int
  
  # Characteristics, stay the same
  sizeX: int
  sizeY: int
  price: int
  
  # Consumed/Produced resources
  consumedPower: int
  consumedCWater: int
  consumedInternalNet: int
  producedDWater: int
  producedDataStorage: int
  connections: dict
  # connections be like: {'input':{}}, where each element in dict represents 1 connection to that object


class DataRack_100(DataRackBase):
  def __init__(self, posX, posY):
    self.posX = posX
    self.posY = posY
    self.sizeX = 40
    self.sizeY = 40
    self.price = 2000
    self.consumedPower = 15
    self.consumedCWater = 3
    self.consumedInternalNet = 5
    self.producedDWater = 3
    self.producedDataStorage = 100
    self.connections = {'input':{}}

class DataRack_250(DataRackBase):
  def __init__(self, posX, posY):
    self.posX = posX
    self.posY = posY
    self.sizeX = 40
    self.sizeY = 40
    self.price = 7500
    self.consumedPower = 25
    self.consumedCWater = 3
    self.consumedInternalNet = 10
    self.producedDWater = 3
    self.producedDataStorage = 250
    self.connections = {'input':{}}

class DataRack_500(DataRackBase):
  def __init__(self, posX, posY):
    self.posX = posX
    self.posY = posY
    self.sizeX = 40
    self.sizeY = 40
    self.price = 20500
    self.consumedPower = 40
    self.consumedCWater = 6
    self.consumedInternalNet = 20
    self.producedDWater = 6
    self.producedDataStorage = 500
    self.connections = {'input':{}}