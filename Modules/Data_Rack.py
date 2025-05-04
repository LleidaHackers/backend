from dataclasses import dataclass
import math
from BaseModule import BaseModule

@dataclass
class DataRackInputs:
    usablePower: int = 0
    chilledWater: int = 0
    internalNetwork: int = 0

@dataclass
class DataRackOutputs:
    distilledWater: int = 0
    dataStorage: int = 0

class DataRackBase(BaseModule):
    def __init__(self, name: str):
        super().__init__(name)
        # Resource consumption/production
        self.consumedPower: int = 0
        self.consumedCWater: int = 0
        self.consumedInternalNet: int = 0
        self.producedDWater: int = 0
        self.producedDataStorage: int = 0
        self.color: str = ""
        
        self.current_inputs = {
            "usablePower": 0, # Default value
            "internalNetwork": 0 , # Default value
            "chilledWater": 0  # Default value
        }
        self.current_outputs = {
            "distilledWater": 0, # Default value
            "dataStorage": 0  # Default value
        }
    def update_outputs(self):
      ##print(f"inputs->{self.current_inputs}")
      self.current_outputs["distilledWater"] = self.current_inputs["chilledWater"]
      usable_power = float(self.current_inputs["usablePower"])
      consumed_power = float(self.consumedPower)
      produced_net = float(self.producedDataStorage)
      ##print(f"astasdata {usable_power / consumed_power}")
      # Perform calculations with floats
      if(usable_power>consumed_power):
        result =  produced_net
      else:
         result = ((usable_power / consumed_power)) * produced_net
      # Convert final result to integer
      self.current_outputs["dataStorage"] = math.trunc(result)
      
      
class DataRack_100(DataRackBase):
  def __init__(self, name):
    super().__init__(name)
    self.sizeX = 40
    self.sizeY = 40
    self.price = 2000
    self.consumedPower = 15
    self.consumedCWater = 3
    self.consumedInternalNet = 5
    self.producedDWater = 3
    self.producedDataStorage = 100
    self.color = "f100ff"
    

class DataRack_250(DataRackBase):
  def __init__(self, name):
    super().__init__(name)
    self.sizeX = 40
    self.sizeY = 40
    self.price = 7500
    self.consumedPower = 25
    self.consumedCWater = 3
    self.consumedInternalNet = 10
    self.producedDWater = 3
    self.producedDataStorage = 250
    self.color = "87358c"


class DataRack_500(DataRackBase):
  def __init__(self, name):
    super().__init__(name)
    self.sizeX = 40
    self.sizeY = 40
    self.price = 20500
    self.consumedPower = 40
    self.consumedCWater = 6
    self.consumedInternalNet = 20
    self.producedDWater = 6
    self.producedDataStorage = 500
    self.color = "5c275f"