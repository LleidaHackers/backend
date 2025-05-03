from BaseModule import BaseModule

class WaterTreatmentBase(BaseModule):
  # Consumed/Produced resources
  consumedFWater: int
  consumedPower: int
  producedDWater: int
  color: str


class WaterTreatment_50(WaterTreatmentBase):
  def __init__(self, name):
    super().__init__(name)
    self.sizeX = 50
    self.sizeY = 50
    self.price = 10000
    self.consumedFWater = 50
    self.consumedPower = 50
    self.producedDWater = 50
    self.color = "ff7000"


class WaterTreatment_250(WaterTreatmentBase):
  def __init__(self, name):
    super().__init__(name)
    self.sizeX = 200
    self.sizeY = 200
    self.price = 40000
    self.consumedFWater = 250
    self.consumedPower = 90
    self.producedDWater = 250
    self.color = "c95a03"


class WaterTreatment_500(WaterTreatmentBase):
  def __init__(self, name):
    super().__init__(name)
    self.sizeX = 400
    self.sizeY = 400
    self.price = 70000
    self.consumedFWater = 500
    self.consumedPower = 150
    self.producedDWater = 500
    self.color = "a54b03"