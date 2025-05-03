from BaseModule import BaseModule

class WaterChillerBase(BaseModule):
  # Consumed/Produced resources
  consumedDWater: int
  consumedPower: int
  producedCWater: int


class WaterChiller_100(WaterChillerBase):
  def __init__(self, posX, posY):
    super().__init__("WaterChiller_100", posX, posY)
    self.sizeX = 100
    self.sizeY = 100
    self.price = 40000
    self.consumedDWater = 100
    self.consumedPower = 500
    self.producedCWater = 95


class WaterChiller_400(WaterChillerBase):
  def __init__(self, posX, posY):
    super().__init__("WaterChiller_400", posX, posY)
    self.sizeX = 300
    self.sizeY = 100
    self.price = 150000
    self.consumedDWater = 400
    self.consumedPower = 1500
    self.producedCWater = 390