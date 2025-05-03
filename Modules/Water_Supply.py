from BaseModule import BaseModule

class WaterSupplyBase(BaseModule):
  # Consumed/Produced resources
  consumedWaterConn: int
  producedFWater: int


class WaterSupply_100(WaterSupplyBase):
  def __init__(self, posX, posY):
    super().__init__("WaterSupply_100", posX, posY)
    self.sizeX = 50
    self.sizeY = 50
    self.price = 200
    self.producedFWater = 100
    self.consumedWaterConn = 1


class WaterSupply_500(WaterSupplyBase):
  def __init__(self, posX, posY):
    super().__init__("WaterSupply_500", posX, posY)
    self.sizeX = 150
    self.sizeY = 100
    self.price = 400
    self.producedFWater = 500
    self.consumedWaterConn = 1