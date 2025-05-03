from threading import Thread
import time
from BaseModule import BaseModule
from dataclasses import dataclass, fields
from paho.mqtt import client as mqtt_client

def in_out_map(input) -> str:
  if(input == "distilledWater"):
    return "chilledWater"
  else:
    None

@dataclass
class WaterChillerInputs:
    distilledWater: int = 0  # Note: Fixed typo from 'distlledWater'
    usablePower: int = 0

@dataclass
class WaterChillerOutputs:
    chilledWater: int = 0

class WaterChillerBase(BaseModule, Thread):
    def __init__(self, name: str):
        Thread.__init__(self, daemon=True)     
        BaseModule.__init__(self, name)  
        # Resource tracking
        self.consumedDWater: int = 0  # Distilled water consumption
        self.consumedPower: int = 0   # Power consumption
        self.producedCWater: int = 0  # Chilled water production
        self.running = False
        self.color: str = ""
        
        # Current state using dataclasses
        self.current_inputs: WaterChillerInputs = WaterChillerInputs()
        self.current_outputs = {
            "chilledWater": 0  # Default value
        }

    def run(self):
        """Start background simulation loop."""
        self.running = True
        client = self.connect_mqtt()
        client.loop_start()
        outputs = list(self.current_outputs.keys())
        topics = [] #[(f"/{self.conn_inputs[0].type}/{self.conn_inputs[0].id}",0),(f"/{self.conn_inputs[1].type}/{self.conn_inputs[1].id}",0),("Server3/kpi3",0)]
        for connection in self.conn_inputs:
          topics.append((f"/{connection.type}/{connection.id}",0))
          
        self.subscribe_child(client,topics,in_out_map)
        while self.running:
          for output in outputs:
            print(f"on pub->{self.current_outputs}")
            self.publish(client,f"/{output}/{self.id}",self.current_outputs[output],self.__module__ )
          time.sleep(1)
            
        client.loop_stop()

    def stop(self):
        """Stop the simulation thread."""
        
        self.running = False
  
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