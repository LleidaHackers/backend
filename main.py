from Modules2.Data_Rack import DataRack_100

trans = DataRack_100(150, 40)
print(trans.connections)
print("Coords: ("+str(trans.posX)+", "+str(trans.posY)+")")
print("Price: " + str(trans.price))
trans.setPos(200, 200)
print("Coords: ("+str(trans.posX)+", "+str(trans.posY)+")")
trans.setInput(1)
trans.setInput(2)
trans.removeInput(1)
print(trans.connections['input'])
