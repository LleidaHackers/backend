from BaseModule import BaseModule
from dataclasses import dataclass

@dataclass
class WaterChillerInputs:
    distilledWater: int = 0  # Note: Fixed typo from 'distlledWater'
    usablePower: int = 0

@dataclass
class WaterChillerOutputs:
    chilledWater: int = 0

class WaterChillerBase(BaseModule):
    def __init__(self, name: str):
        super().__init__(name)
        # Resource tracking
        self.consumedDWater: int = 0  # Distilled water consumption
        self.consumedPower: int = 0   # Power consumption
        self.producedCWater: int = 0  # Chilled water production
        self.color: str = ""
        
        # Current state using dataclasses
        self.current_inputs: WaterChillerInputs = WaterChillerInputs()
        self.current_outputs: WaterChillerOutputs = WaterChillerOutputs()
    

class WaterChiller_100(WaterChillerBase):
  def __init__(self, name):
    super().__init__(name)
    self.sizeX = 100
    self.sizeY = 100
    self.price = 40000
    self.consumedDWater = 100
    self.consumedPower = 500
    self.producedCWater = 95
    self.color = "00fff2"


class WaterChiller_400(WaterChillerBase):
  def __init__(self, name):
    super().__init__(name)
    self.sizeX = 300
    self.sizeY = 100
    self.price = 150000
    self.consumedDWater = 400
    self.consumedPower = 1500
    self.producedCWater = 390
    self.color = "089b94"