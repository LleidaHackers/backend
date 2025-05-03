from BaseModule import BaseModule

class ServerRackBase(BaseModule):
  # Consumed/Produced resources
  consumedPower: int
  consumedCWater: int
  consumedInternalNet: int
  producedDWater: int
  producedProcessing: int
  producedExternalNet: int


class ServerRack_100(ServerRackBase):
  def __init__(self, posX, posY):
    super().__init__("ServerRack_100", posX, posY)
    self.sizeX = 40
    self.sizeY = 40
    self.price = 8000
    self.consumedPower = 75
    self.consumedCWater = 15
    self.consumedInternalNet = 10
    self.producedDWater = 15
    self.producedProcessing = 100
    self.producedExternalNet = 100


class ServerRack_200(ServerRackBase):
  def __init__(self, posX, posY):
    super().__init__("ServerRack_200", posX, posY)
    self.sizeX = 40
    self.sizeY = 40
    self.price =  12000
    self.consumedPower = 125
    self.consumedCWater = 25
    self.consumedInternalNet = 18
    self.producedDWater = 25
    self.producedProcessing = 150
    self.producedExternalNet = 200  


class ServerRack_500(ServerRackBase):
  def __init__(self, posX, posY):
    super().__init__("ServerRack_500", posX, posY)
    self.sizeX = 40
    self.sizeY = 40
    self.price =  50000
    self.consumedPower = 240
    self.consumedCWater = 50
    self.consumedInternalNet = 32
    self.producedDWater = 50
    self.producedProcessing = 1000
    self.producedExternalNet = 400