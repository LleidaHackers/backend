from dataclasses import dataclass, fields
import random
from threading import Thread
import time
from BaseModule import BaseModule

@dataclass
class WaterSupplyInputs:
    waterConnection: int = 0

@dataclass
class WaterSupplyOutputs:
    freshWater: int = 0

class WaterSupplyBase(BaseModule, Thread):
    def __init__(self, name: str):
        Thread.__init__(self, daemon=True)     
        BaseModule.__init__(self, name)  
        # Consumed/Produced resources
        self.consumedWaterConn: int = 0
        self.producedFWater: int = 0
        self.color: str = ""
        self.running = False
        # Current state using dataclasses
        self.current_inputs: WaterSupplyInputs = WaterSupplyInputs()
        self.current_outputs: WaterSupplyOutputs = WaterSupplyOutputs()
        
    def generate(self) -> float:
        """Simulate one second of power output with ±5% variation."""
        error = random.uniform(-0.05, 0.05)
        output = self.producedFWater * (1 + error)
        self.current_outputs.freshWater = int(output)
        return output
    
    def run(self):
        """Start background simulation loop."""
        self.running = True
        client = self.connect_mqtt()
        client.loop_start()
        ##print(f"/transformer/{self.id}")
        #self.subscribe(client,f"/transformer/{self.id}")
        outputs = [field.name for field in fields(WaterSupplyOutputs)]
        while self.running:
            for output in outputs:
              self.current_outputs.freshWater = self.generate()
              self.publish(client,f"/{output}/{self.id}",self.current_outputs.freshWater)
              ##print(f"[{self.name}] {output}: {self.current_outputs.usablePower:.2f} kW")
              
            time.sleep(1)
             
              
        client.loop_stop()

    def stop(self):
        """Stop the simulation thread."""
        self.running = False
        
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