class WaterSupplyBase:
  # Position, may vary
  posX: int
  posY: int
  
  # Characteristics, stay the same
  sizeX: int
  sizeY: int
  price: int
  
  # Consumed/Produced resources
  consumedWaterConn: int
  producedFWater: int
  connections: dict
  # connections be like: {'input':{}}, where each element in dict represents 1 connection to that object


class WaterSupply_100(WaterSupplyBase):
  def __init__(self, posX, posY):
    self.posX = posX
    self.posY = posY
    self.sizeX = 50
    self.sizeY = 50
    self.price = 200
    self.producedFWater = 100
    self.consumedWaterConn = 1
    self.connections = {'input':{}, 'output':{}}


class WaterSupply_100(WaterSupplyBase):
  def __init__(self, posX, posY):
    self.posX = posX
    self.posY = posY
    self.sizeX = 150
    self.sizeY = 100
    self.price = 400
    self.producedFWater = 500
    self.consumedWaterConn = 1
    self.connections = {'input':{}, 'output':{}}