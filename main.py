from Modules.Transformer import Transformer

data_rack = Transformer("Rack01", 1)
print(data_rack.name)  # prints "Rack01"
data_rack.posX = 123
print(data_rack.posX)
