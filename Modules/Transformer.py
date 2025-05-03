from dataclasses import dataclass
from threading import Thread
import random
import time

from BaseModule import BaseModule  # keep this import as per your structure

@dataclass
class TransformerInputs:
    gridConnection: int = 0

@dataclass
class TransformerOutputs:
    usablePower: float = 0

class TransformerBase(BaseModule, Thread):
    def __init__(self, name):
        Thread.__init__(self, daemon=True)          # FIRST: initialize thread
        BaseModule.__init__(self, name)             # THEN: initialize your base module
        self.current_inputs : TransformerInputs = TransformerInputs()
        self.current_outputs : TransformerOutputs = TransformerOutputs()
        self.running = False
        
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

        self.publish(client,f"/transformer/{self.id}")
        """"        while self.running:
            self.current_outputs.usablePower = self.generate()
            print(f"[{self.name}] Power Output: {self.current_outputs.usablePower:.2f} kW")
            time.sleep(1)
            self.publish(client,"/test/topic")"""
            
        client.loop_stop()

    def stop(self):
        """Stop the simulation thread."""
        self.running = False

# Subclasses stay the same, just inherit threading via TransformerBase

class Transformer_100(TransformerBase):
    def __init__(self, name):
        super().__init__(name)
        self.sizeX = 40
        self.sizeY = 45
        self.price = 1000
        self.consumedGridConn = 1
        self.producedPower = 100
        self.color = "00ff4a"

class Transformer_1000(TransformerBase):
    def __init__(self, name):
        super().__init__(name)
        self.sizeX = 100
        self.sizeY = 100
        self.price = 50000
        self.consumedGridConn = 1
        self.producedPower = 1000
        self.color = "0cbb3f"

class Transformer_5000(TransformerBase):
    def __init__(self, name):
        super().__init__(name)
        self.sizeX = 200
        self.sizeY = 200
        self.price = 250000
        self.consumedGridConn = 1
        self.producedPower = 5000
        self.color = "048229"
