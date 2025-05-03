from BaseModule import BaseModule

class WaterSupplyBase(BaseModule):
  # Consumed/Produced resources
  consumedWaterConn: int
  producedFWater: int


class WaterSupply_100(WaterSupplyBase):
  def __init__(self, posX, posY):
    self.posX = posX
    self.posY = posY
    self.sizeX = 50
    self.sizeY = 50
    self.price = 200
    self.producedFWater = 100
    self.consumedWaterConn = 1


class WaterSupply_100(WaterSupplyBase):
  def __init__(self, posX, posY):
    self.posX = posX
    self.posY = posY
    self.sizeX = 150
    self.sizeY = 100
    self.price = 400
    self.producedFWater = 500
    self.consumedWaterConn = 1