from BaseModule import BaseModule

class WaterTreatmentBase(BaseModule):
  # Consumed/Produced resources
  consumedFWater: int
  consumedPower: int
  producedDWater: int


class WaterTreatment_50(WaterTreatmentBase):
  def __init__(self, posX, posY):
    self.posX = posX
    self.posY = posY
    self.sizeX = 50
    self.sizeY = 50
    self.price = 10000
    self.consumedFWater = 50
    self.consumedPower = 50
    self.producedDWater = 50


class WaterTreatment_250(WaterTreatmentBase):
  def __init__(self, posX, posY):
    self.posX = posX
    self.posY = posY
    self.sizeX = 200
    self.sizeY = 200
    self.price = 40000
    self.consumedFWater = 250
    self.consumedPower = 90
    self.producedDWater = 250


class WaterTreatment_500(WaterTreatmentBase):
  def __init__(self, posX, posY):
    self.posX = posX
    self.posY = posY
    self.sizeX = 400
    self.sizeY = 400
    self.price = 70000
    self.consumedFWater = 500
    self.consumedPower = 150
    self.producedDWater = 500