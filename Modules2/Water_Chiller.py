class WaterChillerBase:
  # Position, may vary
  posX: int
  posY: int
  
  # Characteristics, stay the same
  sizeX: int
  sizeY: int
  price: int
  
  # Consumed/Produced resources
  consumedDWater: int
  consumedPower: int
  producedCWater: int
  connections: dict
  # connections be like: {'input':{}}, where each element in dict represents 1 connection to that object


class WaterChiller_100(WaterChillerBase):
  def __init__(self, posX, posY):
    self.posX = posX
    self.posY = posY
    self.sizeX = 100
    self.sizeY = 100
    self.price = 40000
    self.consumedDWater = 100
    self.consumedPower = 500
    self.producedCWater = 95
    self.connections = {'input':{}, 'output':{}}


class WaterChiller_400(WaterChillerBase):
  def __init__(self, posX, posY):
    self.posX = posX
    self.posY = posY
    self.sizeX = 300
    self.sizeY = 100
    self.price = 150000
    self.consumedDWater = 400
    self.consumedPower = 1500
    self.producedCWater = 390
    self.connections = {'input':{}, 'output':{}}