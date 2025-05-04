from dataclasses import dataclass
import math
import random
from threading import Thread
import time
from BaseModule import BaseModule
from paho.mqtt import client as mqtt_client
@dataclass
class NetworkRackInputs:
    usablePower: int = 0
    chilledWater: int = 0

@dataclass
class NetworkRackOutputs:
    internalNetwork: int = 0
    freshWater: int = 0

class NetworkRackBase(BaseModule, Thread):
    def __init__(self, name: str):
        Thread.__init__(self, daemon=True)
        BaseModule.__init__(self, name) 
        # Resource consumption/production
        self.consumedPower: int = 0
        self.consumedCWater: int = 0
        self.producedFWater: int = 0
        self.producedInternalNet: int = 0
        self.color: str = ""
        self.running = False
        # Current state using dataclasses
        self.current_inputs = {
            "usablePower": 0, # Default value
            "chilledWater": 0  # Default value
        }
        self.current_outputs = {
            "internalNetwork": 0, # Default value
            "freshWater": 0  # Default value
        }
    def update_outputs(self):
      ##print(f"inputs->{self.current_inputs}")
      self.current_outputs["freshWater"] = self.current_inputs["chilledWater"]
      usable_power = float(self.current_inputs["usablePower"])
      consumed_power = float(self.consumedPower)
      produced_net = float(self.producedInternalNet)
      ##print(f"astasdata {usable_power / consumed_power}")
      # Perform calculations with floats
      if(usable_power>consumed_power):
        result =  produced_net
      else:
         result = ((usable_power / consumed_power)) * produced_net
      # Convert final result to integer
      self.current_outputs["internalNetwork"] = math.trunc(result)
    def in_out_map(self, input) -> str:
      if(input == "chilledWater"):
        return "freshWater"
      else:
        None
        
 
        
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