from dataclasses import dataclass
from BaseModule import BaseModule

@dataclass
class ServerRackInputs:
    usablePower: int = 0
    chilledWater: int = 0
    internalNetwork: int = 0

@dataclass
class ServerRackOutputs:
    distilledWater: int = 0
    processing: int = 0
    externalNetwork: int = 0

class ServerRackBase(BaseModule):
    def __init__(self, name: str):
        super().__init__(name)
        # Resource consumption/production
        self.consumedPower: int = 0
        self.consumedCWater: int = 0
        self.consumedInternalNet: int = 0
        self.producedDWater: int = 0
        self.producedProcessing: int = 0
        self.producedExternalNet: int = 0
        self.color: str = ""
        
        # Current state
        self.current_inputs = ServerRackInputs()
        self.current_outputs = ServerRackOutputs()
        
        
class ServerRack_100(ServerRackBase):
  def __init__(self, name):
    super().__init__(name)
    self.sizeX = 40
    self.sizeY = 40
    self.price = 8000
    self.consumedPower = 75
    self.consumedCWater = 15
    self.consumedInternalNet = 10
    self.producedDWater = 15
    self.producedProcessing = 100
    self.producedExternalNet = 100
    self.color = "ff0000"


class ServerRack_200(ServerRackBase):
  def __init__(self, name):
    super().__init__(name)
    self.sizeX = 40
    self.sizeY = 40
    self.price =  12000
    self.consumedPower = 125
    self.consumedCWater = 25
    self.consumedInternalNet = 18
    self.producedDWater = 25
    self.producedProcessing = 150
    self.producedExternalNet = 200
    self.color = "b70505"


class ServerRack_500(ServerRackBase):
  def __init__(self, name):
    super().__init__(name)
    self.sizeX = 40
    self.sizeY = 40
    self.price =  50000
    self.consumedPower = 240
    self.consumedCWater = 50
    self.consumedInternalNet = 32
    self.producedDWater = 50
    self.producedProcessing = 1000
    self.producedExternalNet = 400
    self.color = "8c0101"