class ServerRackBase:
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
  producedProcessing: int
  producedExternalNet: int
  connections: dict
  # connections be like: {'input':{}, 'output':{}}, where each element in dict represents 1 connection to that object


class ServerRack_50(ServerRackBase):
  def __init__(self, posX, posY):
    self.posX = posX
    self.posY = posY
    self.sizeX = 40
    self.sizeY = 40
    self.prize = 8000
    self.consumedPower = 75
    self.consumedCWater = 15
    self.consumedInternalNet = 10
    self.producedDWater = 15
    self.producedProcessing = 100
    self.producedExternalNet = 100
    self.connections = {'input':{}}


class ServerRack_200(ServerRackBase):
  def __init__(self, posX, posY):
    self.posX = posX
    self.posY = posY
    self.sizeX = 40
    self.sizeY = 40
    self.prize =  12000
    self.consumedPower = 125
    self.consumedCWater = 25
    self.consumedInternalNet = 18
    self.producedDWater = 25
    self.producedProcessing = 150
    self.producedExternalNet = 200
    self.connections = {'input':{}}


class ServerRack_500(ServerRackBase):
  def __init__(self, posX, posY):
    self.posX = posX
    self.posY = posY
    self.sizeX = 40
    self.sizeY = 40
    self.prize =  50000
    self.consumedPower = 240
    self.consumedCWater = 50
    self.consumedInternalNet = 32
    self.producedDWater = 50
    self.producedProcessing = 1000
    self.producedExternalNet = 400
    self.connections = {'input':{}}