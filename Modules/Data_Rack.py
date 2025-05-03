from BaseModule import BaseModule

class DataRackBase(BaseModule):
  # Consumed/Produced resources
  consumedPower: int
  consumedCWater: int
  consumedInternalNet: int
  producedDWater: int
  producedDataStorage: int
  

class DataRack_100(DataRackBase):
  def __init__(self, name, posX, posY):
    super().__init__(name, posX, posY)
    self.sizeX = 40
    self.sizeY = 40
    self.price = 2000
    self.consumedPower = 15
    self.consumedCWater = 3
    self.consumedInternalNet = 5
    self.producedDWater = 3
    self.producedDataStorage = 100
    

class DataRack_250(DataRackBase):
  def __init__(self, name, posX, posY):
    super().__init__(name, posX, posY)
    self.sizeX = 40
    self.sizeY = 40
    self.price = 7500
    self.consumedPower = 25
    self.consumedCWater = 3
    self.consumedInternalNet = 10
    self.producedDWater = 3
    self.producedDataStorage = 250


class DataRack_500(DataRackBase):
  def __init__(self, name, posX, posY):
    super().__init__(name, posX, posY)
    self.sizeX = 40
    self.sizeY = 40
    self.price = 20500
    self.consumedPower = 40
    self.consumedCWater = 6
    self.consumedInternalNet = 20
    self.producedDWater = 6
    self.producedDataStorage = 500