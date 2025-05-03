class TransformerBase:
  # Position, may vary
  posX: int
  posY: int
  
  # Characteristics, stay the same
  sizeX: int
  sizeY: int
  price: int
  
  # Consumed/Produced resources
  consumedGridConn: int
  producedPower: int
  connections: dict
  # connections be like: {'input':{}}, where each element in dict represents 1 connection to that object


class Transformer_100(TransformerBase):
  def __init__(self, posX, posY):
    self.posX = posX
    self.posY = posY
    self.sizeX = 40
    self.sizeY = 45
    self.prize = 1000
    self.consumedGridConn = 1
    self.producedPower = 100
    self.connections = {'input':{}, 'output':{}}


class Transformer_1000(TransformerBase):
  def __init__(self, posX, posY):
    self.posX = posX
    self.posY = posY
    self.sizeX = 100
    self.sizeY = 100
    self.prize = 50000
    self.consumedGridConn = 1
    self.producedPower = 1000
    self.connections = {'input':{}, 'output':{}}


class Transformer_5000(TransformerBase):
  def __init__(self, posX, posY):
    self.posX = posX
    self.posY = posY
    self.sizeX = 200
    self.sizeY = 200
    self.prize = 250000
    self.consumedGridConn = 1
    self.producedPower = 5000
    self.connections = {'input':{}, 'output':{}}