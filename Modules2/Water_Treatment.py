class WaterTreatmentBase:
  # Position, may vary
  posX: int
  posY: int
  
  # Characteristics, stay the same
  sizeX: int
  sizeY: int
  price: int
  
  # Consumed/Produced resources
  consumedFWater: int
  consumedPower: int
  producedDWater: int
  connections: dict
  # connections be like: {'input':{}}, where each element in dict represents 1 connection to that object


class WaterTreatment_100(WaterTreatmentBase):
  def __init__(self, posX, posY):
    self.posX = posX
    self.posY = posY
    self.sizeX = 50
    self.sizeY = 50
    self.prize = 10000
    self.consumedFWater = 50
    self.consumedPower = 50
    self.producedDWater = 50
    self.connections = {'input':{}, 'output':{}}



class WaterTreatment_100(WaterTreatmentBase):
  def __init__(self, posX, posY):
    self.posX = posX
    self.posY = posY
    self.sizeX = 50
    self.sizeY = 50
    self.prize = 10000
    self.consumedFWater = 250
    self.consumedPower = 90
    self.producedDWater = 250
    self.connections = {'input':{}, 'output':{}}



class WaterTreatment_500(WaterTreatmentBase):
  def __init__(self, posX, posY):
    self.posX = posX
    self.posY = posY
    self.sizeX = 50
    self.sizeY = 50
    self.prize = 10000
    self.consumedFWater = 500
    self.consumedPower = 150
    self.producedDWater = 500
    self.connections = {'input':{}, 'output':{}}