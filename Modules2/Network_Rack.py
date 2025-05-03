from BaseModule import BaseModule

class NetworkRackBase(BaseModule):
  # Consumed/Produced resources
  consumedPower: int
  consumedCWater: int
  producedFWater: int
  producedInternalNet: int


class NetworkRack_50(NetworkRackBase):
  def __init__(self, posX, posY):
    super().__init__("NetworkRack_50", posX, posY)
    self.sizeX = 40
    self.sizeY = 40
    self.price = 2000
    self.consumedPower = 50
    self.consumedCWater = 5
    self.producedInternalNet = 50
    self.producedFWater = 5
    

class NetworkRack_100(NetworkRackBase):
  def __init__(self, posX, posY):
    super().__init__("NetworkRack_100", posX, posY)
    self.sizeX = 40
    self.sizeY = 40
    self.price = 8000
    self.consumedPower = 75
    self.consumedCWater = 7
    self.producedInternalNet = 100
    self.producedFWater = 7
    

class NetworkRack_200(NetworkRackBase):
  def __init__(self, posX, posY):
    super().__init__("NetworkRack_200", posX, posY)
    self.sizeX = 40
    self.sizeY = 40
    self.price = 20000
    self.consumedPower = 95
    self.consumedCWater = 10
    self.producedInternalNet = 200
    self.producedFWater = 40