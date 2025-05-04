class BaseModule:
  id: str # Given from frontend
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
    self.id=0
    self.name = name
    self.posX = 0
    self.posY = 0

    self.connectedIn = []
    self.connectedOut = []

    self.color = "#FF0000"
    self.posX = 0
    self.posY = 0
    self.connections = {
      'input': [],
      'output': []
    }

  
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

