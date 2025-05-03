class NetworkRackBase:
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
  producedFWater: int
  producedInternalNet: int
  connections: dict
  # connections be like: {'input':{}, 'output':{}}, where each element in dict represents 1 connection to that object


class NetworkRack_50(NetworkRackBase):
  def __init__(self, posX, posY):
    self.posX = posX
    self.posY = posY
    self.sizeX = 40
    self.sizeY = 40
    self.price = 2000
    self.consumedPower = 50
    self.consumedCWater = 5
    self.producedInternalNet = 50
    self.producedFWater = 5
    self.connections = {'input':{}, 'output':{}}

class NetworkRack_100(NetworkRackBase):
  def __init__(self, posX, posY):
    self.posX = posX
    self.posY = posY
    self.sizeX = 40
    self.sizeY = 40
    self.price = 8000
    self.consumedPower = 75
    self.consumedCWater = 7
    self.producedInternalNet = 100
    self.producedFWater = 7
    self.connections = {'input':{}, 'output':{}}

class NetworkRack_200(NetworkRackBase):
  def __init__(self, posX, posY):
    self.posX = posX
    self.posY = posY
    self.sizeX = 40
    self.sizeY = 40
    self.price = 20000
    self.consumedPower = 95
    self.consumedCWater = 10
    self.producedInternalNet = 200
    self.producedFWater = 40
    self.connections = {'input':{}, 'output':{}}