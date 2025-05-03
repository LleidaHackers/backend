from BaseModule import BaseModule

class WaterChillerBase(BaseModule):
  # Consumed/Produced resources
  consumedDWater: int
  consumedPower: int
  producedCWater: int
  color: str


class WaterChiller_100(WaterChillerBase):
  def __init__(self, name):
    super().__init__(name)
    self.sizeX = 100
    self.sizeY = 100
    self.price = 40000
    self.consumedDWater = 100
    self.consumedPower = 500
    self.producedCWater = 95
    self.color = "00fff2"


class WaterChiller_400(WaterChillerBase):
  def __init__(self, name):
    super().__init__(name)
    self.sizeX = 300
    self.sizeY = 100
    self.price = 150000
    self.consumedDWater = 400
    self.consumedPower = 1500
    self.producedCWater = 390
    self.color = "089b94"