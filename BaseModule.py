from random import randint

class BaseModule:
  id: int # Given from frontend
  name: str
  # Position, will vary in the future (after solving for positioning)
  posX: int
  posY: int
  # Characteristics, stay the same, will be set when
  sizeX: int
  sizeY: int
  price: int

  connectedIn: list[str] # List of ids of connected modules
  connectedOut: list[str] # List of ids of connected modules


  def __init__(self, name):
    self.name = name
    self.posX = 0
    self.posY = 0
    self.connectedIn = []
    self.connectedOut = []