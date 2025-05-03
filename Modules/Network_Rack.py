from dataclasses import dataclass
from BaseModule import BaseModule

@dataclass
class NetworkRackInputs:
    usablePower: int = 0
    chilledWater: int = 0

@dataclass
class NetworkRackOutputs:
    internalNetwork: int = 0
    freshWater: int = 0

class NetworkRackBase(BaseModule):
    def __init__(self, name: str):
        super().__init__(name)
        # Resource consumption/production
        self.consumedPower: int = 0
        self.consumedCWater: int = 0
        self.producedFWater: int = 0
        self.producedInternalNet: int = 0
        self.color: str = ""
        
        # Current state using dataclasses
        self.current_inputs = NetworkRackInputs()
        self.current_outputs = NetworkRackOutputs()

class NetworkRack_50(NetworkRackBase):
  def __init__(self, name):
    super().__init__(name)
    self.sizeX = 40
    self.sizeY = 40
    self.price = 2000
    self.consumedPower = 50
    self.consumedCWater = 5
    self.producedInternalNet = 50
    self.producedFWater = 5
    self.color = "0089ff"
    

class NetworkRack_100(NetworkRackBase):
  def __init__(self, name):
    super().__init__(name)
    self.sizeX = 40
    self.sizeY = 40
    self.price = 8000
    self.consumedPower = 75
    self.consumedCWater = 7
    self.producedInternalNet = 100
    self.producedFWater = 7
    self.color = "89bce9"    

class NetworkRack_200(NetworkRackBase):
  def __init__(self, name):
    super().__init__(name)
    self.sizeX = 40
    self.sizeY = 40
    self.price = 20000
    self.consumedPower = 95
    self.consumedCWater = 10
    self.producedInternalNet = 200
    self.producedFWater = 40
    self.color = "0f3e67"