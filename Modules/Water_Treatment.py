from dataclasses import dataclass
from BaseModule import BaseModule

@dataclass
class WaterTreatmentInputs:
    freshWater: int = 0
    usablePower: int = 0

@dataclass
class WaterTreatmentOutputs:
    distilledWater: int = 0  # Fixed typo from 'distlledWater'

class WaterTreatmentBase(BaseModule):
    def __init__(self, name: str):
        super().__init__(name)
        # Consumed/Produced resources
        self.consumedFWater: int = 0
        self.consumedPower: int = 0
        self.producedDWater: int = 0
        self.color: str = ""
        
        # Current state using dataclasses
        self.current_inputs = {
            "freshWater": 0,  # Default value
            "usablePower": 0
        }
        self.current_outputs = {
            "distilledWater": 0  # Default value
        }
    def update_outputs(self):
      #print(f"inputs->{self.current_inputs}")
      self.current_outputs["distilledWater"] = self.current_inputs["freshWater"]
      
    def in_out_map(self, input) -> str:
      if(input == "freshWater"):
        return "distilledWater"
      else:
        None
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