from BaseModule import BaseModule

class TransformerBase(BaseModule):
  # Consumed/Produced resources
  consumedGridConn: int
  producedPower: int


class Transformer_100(TransformerBase):
  def __init__(self, posX, posY):
    super().__init__("Transformer_100", posX, posY)
    self.sizeX = 40
    self.sizeY = 45
    self.price = 1000
    self.consumedGridConn = 1
    self.producedPower = 100


class Transformer_1000(TransformerBase):
  def __init__(self, posX, posY):
    super().__init__("Transformer_1000", posX, posY)
    self.sizeX = 100
    self.sizeY = 100
    self.price = 50000
    self.consumedGridConn = 1
    self.producedPower = 1000


class Transformer_5000(TransformerBase):
  def __init__(self, posX, posY):
    super().__init__("Transformer_5000", posX, posY)
    self.sizeX = 200
    self.sizeY = 200
    self.price = 250000
    self.consumedGridConn = 1
    self.producedPower = 5000