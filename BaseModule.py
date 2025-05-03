import random

class BaseModule:
  id: int
  name: str
  # Position, may vary
  posX: int
  posY: int
  # Characteristics, stay the same, will be set when
  sizeX: int
  sizeY: int
  price: int
  # Connection with other modules
  connections: dict 

  def __init__(self, name, posX, posY):
    self.id = random.randint(0, 1000000)  # Random ID for the module
    self.name = name
    self.posX = posX
    self.posY = posY
    self.connections = {
      'input': [],
      'output': []
    }

  def setPos(self, posX, posY):
    self.posX = posX
    self.posY = posY
  
  def setInput(self, other_object_id):
    if other_object_id in self.connections['input']:
      print(f"Input connection with ID {other_object_id} already exists.")
    else:
      self.connections['input'].append(other_object_id)

  def setOutput(self, other_object_id):
    if other_object_id in self.connections['output']:
      print(f"Output connection with ID {other_object_id} already exists.")
    else:
      self.connections['output'].append(other_object_id)

  def removeInput(self, other_object_id):
    if other_object_id in self.connections['input']:
      self.connections['input'].remove(other_object_id)
    else:
      print(f"Input connection with ID {other_object_id} not found for removal.")

  def removeOutput(self, other_object_id):
    if other_object_id in self.connections['output']:
      self.connections['output'].remove(other_object_id)
    else:
      print(f"output connection with ID {other_object_id} not found for removal.")