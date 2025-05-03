from dataclasses import dataclass
from BaseModule import BaseModule

@dataclass
class WaterSupplyInputs:
    waterConnection: int = 0

@dataclass
class WaterSupplyOutputs:
    freshWater: int = 0

class WaterSupplyBase(BaseModule):
    def __init__(self, name: str):
        super().__init__(name)
        # Consumed/Produced resources
        self.consumedWaterConn: int = 0
        self.producedFWater: int = 0
        self.color: str = ""
        
        # Current state using dataclasses
        self.current_inputs: WaterSupplyInputs = WaterSupplyInputs()
        self.current_outputs: WaterSupplyOutputs = WaterSupplyOutputs()

class WaterSupply_100(WaterSupplyBase):
  def __init__(self, name):
    super().__init__(name)
    self.sizeX = 50
    self.sizeY = 50
    self.price = 200
    self.producedFWater = 100
    self.consumedWaterConn = 1
    self.color = "004aff"


class WaterSupply_500(WaterSupplyBase):
  def __init__(self, name):
    super().__init__(name)
    self.sizeX = 150
    self.sizeY = 100
    self.price = 400
    self.producedFWater = 500
    self.consumedWaterConn = 1
    self.color = "0339ba"