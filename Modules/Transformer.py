from dataclasses import dataclass
from BaseModule import BaseModule

@dataclass
class TransformerInputs:
    gridConnection: int = 0  # Note: Fixed typo from 'gridConenction'

@dataclass
class TransformerOutputs:
    usablePower: int = 0

class TransformerBase(BaseModule):
  # Consumed/Produced resources
  consumedGridConn: int
  producedPower: int
  color: str
  def __init__(self, name):
    super().__init__(name)
    self.current_inputs:TransformerInputs = TransformerInputs()
    self.current_outputs:TransformerOutputs = TransformerOutputs()



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