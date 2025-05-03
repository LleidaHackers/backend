from dataclasses import dataclass
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
        self.current_inputs = NetworkRackInputs()
        self.current_outputs = NetworkRackOutputs()
        
    def generate(self) -> float:
        """Simulate one second of power output with ±5% variation."""
        error = random.uniform(-0.05, 0.05)
        output = self.producedPower * (1 + error)
        self.current_outputs.usablePower = int(output)
        return output
    
    def run(self):
        """Start background simulation loop."""
        self.running = True
        client = self.connect_mqtt()
        client.loop_start()
        for connection in self.conn_inputs:
          print(f"/{connection.type}/{connection.id}")
          self.subscribe(client,f"/{connection.type}/{connection.id}")
          
        msg_count =0
        while True:
            time.sleep(1)
            msg_count += 1
            if msg_count > 5:
                break
        #self.publish(client,f"/NetworkRack/{self.id}")
        """"        while self.running:
            self.current_outputs.usablePower = self.generate()
            print(f"[{self.name}] Power Output: {self.current_outputs.usablePower:.2f} kW")
            time.sleep(1)
            self.publish(client,"/test/topic")"""
            
        client.loop_stop()

    def stop(self):
        """Stop the simulation thread."""
        self.running = False
        
    def subscribe(self, client: mqtt_client, topic):
    # First call parent's implementation
      super().subscribe(client, topic)
      def child_on_message(client, userdata, msg):
          print(f"Enhanced message handling: {msg.payload.decode()}")
      client.on_message = child_on_message
        
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