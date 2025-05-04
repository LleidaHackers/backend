import time
from Modules.Transformer import Transformer_100, Transformer_1000, Transformer_5000
from Modules.Water_Supply import WaterSupply_100, WaterSupply_500
from Modules.Water_Treatment import WaterTreatment_50, WaterTreatment_250, WaterTreatment_500
from Modules.Water_Chiller import WaterChiller_100, WaterChiller_400
from Modules.Network_Rack import NetworkRack_50, NetworkRack_100, NetworkRack_200
from Modules.Server_Rack import ServerRack_100, ServerRack_200, ServerRack_500
from Modules.Data_Rack import DataRack_100, DataRack_250, DataRack_500
from Connection import Connection
# Create an instance of each module
water_chiller_100 = WaterChiller_100("9")
transformer_100 = Transformer_100("1")
transformer_1000 = Transformer_1000("2")
transformer_5000 = Transformer_5000("3")
water_supply_100 = WaterSupply_100("4")
water_supply_500 = WaterSupply_500("5")
water_treatment_50 = WaterTreatment_50("6")
water_treatment_250 = WaterTreatment_250("7")
water_treatment_500 = WaterTreatment_500("8")
water_chiller_100 = WaterChiller_100("9")
water_chiller_400 = WaterChiller_400("10")
network_rack_50 = NetworkRack_50("11")
network_rack_100 = NetworkRack_100("12")
network_rack_200 = NetworkRack_200("13")
server_rack_100 = ServerRack_100("14")
server_rack_200 = ServerRack_200("15")
server_rack_500 = ServerRack_500("16")
data_rack_100_1 = DataRack_100("17")
data_rack_100_2 = DataRack_100("20")
data_rack_250 = DataRack_250("18")
data_rack_500 = DataRack_500("19")


transformer_5000.id="transformer"
water_supply_500.id="water_supply"
water_treatment_250.id="water_treatment"
water_chiller_400.id="water_chiller"
network_rack_100.id="network_rack"
data_rack_100_1.id="data_rack_1"
server_rack_100.id="server_rack"
data_rack_100_1.id="data_rack_1"
data_rack_500.id="data_rack_2"


transformer_5000.current_inputs.gridConnection = 12341

water_treatment_250.conn_inputs.append(Connection("freshWater",water_supply_500.id))
water_treatment_250.conn_inputs.append(Connection("usablePower",transformer_5000.id))

water_chiller_400.conn_inputs.append(Connection("distilledWater",water_treatment_250.id))
water_chiller_400.conn_inputs.append(Connection("usablePower",transformer_5000.id))

network_rack_100.conn_inputs.append(Connection("chilledWater",water_chiller_400.id))
network_rack_100.conn_inputs.append(Connection("usablePower",transformer_5000.id))

server_rack_100.conn_inputs.append(Connection("usablePower",transformer_5000.id))
server_rack_100.conn_inputs.append(Connection("chilledWater",water_chiller_400.id))
server_rack_100.conn_inputs.append(Connection("internalNetwork",network_rack_100.id))

data_rack_100_1.conn_inputs.append(Connection("usablePower",transformer_5000.id))
data_rack_100_1.conn_inputs.append(Connection("chilledWater",water_chiller_400.id))
data_rack_100_1.conn_inputs.append(Connection("internalNetwork",network_rack_100.id))

data_rack_500.conn_inputs.append(Connection("usablePower",transformer_5000.id))
data_rack_500.conn_inputs.append(Connection("chilledWater",water_chiller_400.id))
data_rack_500.conn_inputs.append(Connection("internalNetwork",network_rack_100.id))




transformer_5000.start()
water_supply_500.start()
water_treatment_250.start()
water_chiller_400.start()
network_rack_100.start()
server_rack_100.start()
data_rack_100_1.start()
data_rack_500.start()



try:
    while(True):
        time.sleep(10)  # Let them run for 5 seconds
        transformer_5000.low=True
        time.sleep(10) 
        transformer_5000.low=False
finally:
    transformer_100.stop()
    network_rack_50.stop()
    #print("Transformers stopped.")