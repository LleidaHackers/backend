def parseTransformer(data):
    """
    Parses the transformer data and returns a Transformer object.
    """
    from Modules.Transformer import Transformer_100, Transformer_1000, Transformer_5000

    type = data['id'].split('-')[0]
    new_object = None
    name = data['data']['label'].split('\n')[0]
    match type:
        case 'transformer_100':
            new_object = Transformer_100(name)
        case 'transformer_1000':
            new_object = Transformer_1000(name)
        case 'transformer_5000':
            new_object = Transformer_5000(name)
        case _:
            raise ValueError(f"This item is not a transformer: {name}")
    

    return new_object if new_object is not None else f"Something went wrong while parsing the following transformer data: {name}."


def parseWaterSupply(data):
    """
    Parses the water supply data and returns a WaterSupply object.
    """
    from Modules.Water_Supply import WaterSupply_100, WaterSupply_500
    type = data['id'].split('-')[0]
    new_object = None
    name = data['data']['label'].split('\n')[0]
    match type:
        case 'water_supply_100':
            new_object = WaterSupply_100(name)
        case 'water_supply_500':
            new_object = WaterSupply_500(name)
        case _:
            raise ValueError(f"This item is not a water supply: {name}")
    

    return new_object if new_object is not None else f"Something went wrong while parsing the following water supply data: {name}."


def parseWaterTreatment(data):
    """
    Parses the water treatment data and returns a WaterTreatment object.
    """
    from Modules.Water_Treatment import WaterTreatment_50, WaterTreatment_250, WaterTreatment_500
    type = data['id'].split('-')[0]
    new_object = None
    name = data['data']['label'].split('\n')[0]
    match type:
        case 'water_treatment_50':
            new_object = WaterTreatment_50(name)
        case 'water_treatment_250':
            new_object = WaterTreatment_250(name)
        case 'water_treatment_500':
            new_object = WaterTreatment_500(name)
        case _:
            raise ValueError(f"This item is not a water treatment: {name}")
    

    return new_object if new_object is not None else f"Something went wrong while parsing the following water treatment data: {name}."


def parseWaterChiller(data):
    """
    Parses the water chiller data and returns a WaterChiller object.
    """
    from Modules.Water_Chiller import WaterChiller_100, WaterChiller_400
    type = data['id'].split('-')[0]
    new_object = None
    name = data['data']['label'].split('\n')[0]
    match type:
        case 'water_chiller_100':
            new_object = WaterChiller_100(name)
        case 'water_chiller_400':
            new_object = WaterChiller_400(name)
        case _:
            raise ValueError(f"This item is not a water chiller: {name}")
    

    return new_object if new_object is not None else f"Something went wrong while parsing the following water chiller data: {name}."


def parseNetworkRack(data):
    """
    Parses the network rack data and returns a NetworkRack object.
    """
    from Modules.Network_Rack import NetworkRack_50, NetworkRack_100, NetworkRack_200
    type = data['id'].split('-')[0]
    new_object = None
    name = data['data']['label'].split('\n')[0]
    match type:
        case 'network_rack_50':
            new_object = NetworkRack_50(name)
        case 'network_rack_100':
            new_object = NetworkRack_100(name)
        case 'network_rack_200':
            new_object = NetworkRack_200(name)
        case _:
            raise ValueError(f"This item is not a network rack: {name}")
    

    return new_object if new_object is not None else f"Something went wrong while parsing the following network rack data: {name}."


def parseServerRack(data):
    """
    Parses the server rack data and returns a ServerRack object.
    """
    from Modules.Server_Rack import ServerRack_100, ServerRack_200, ServerRack_500
    type = data['id'].split('-')[0]
    new_object = None
    name = data['data']['label'].split('\n')[0]
    match type:
        case 'server_rack_100':
            new_object = ServerRack_100(name)
        case 'server_rack_200':
            new_object = ServerRack_200(name)
        case 'server_rack_500':
            new_object = ServerRack_500(name)
        case _:
            raise ValueError(f"This item is not a server rack: {name}")
    

    return new_object if new_object is not None else f"Something went wrong while parsing the following server rack data: {name}."


def parseDataRack(data):
    """
    Parses the data rack data and returns a DataRack object.
    """
    from Modules.Data_Rack import DataRack_100, DataRack_250, DataRack_500
    type = data['id'].split('-')[0]
    new_object = None
    name = data['data']['label'].split('\n')[0]
    match type:
        case 'data_rack_100':
            new_object = DataRack_100(name)
        case 'data_rack_250':
            new_object = DataRack_250(name)
        case 'data_rack_500':
            new_object = DataRack_500(name)
        case _:
            pass  # Proves del fastapi, bd plena de merda i nulls.
    

    return new_object if new_object is not None else f"Something went wrong while parsing the following data rack data: {name}."


def parseModule(data):
    """
    Parses the module data and returns the corresponding object, with only the correct attributes.
    """
    module_type = data['data']['type']

    match module_type:
        case 'transformer':
            return parseTransformer(data)
        case 'water_supply':
            return parseWaterSupply(data)
        case 'water_treatment':
            return parseWaterTreatment(data)
        case 'water_chiller':
            return parseWaterChiller(data)
        case 'network_rack':
            return parseNetworkRack(data)
        case 'server_rack':
            return parseServerRack(data)
        case 'data_rack':
            return parseDataRack(data)
        case _:
            raise ValueError(f"Unknown module type: {module_type}")
        

def parseConnections(data):
    """
    Parses the connections data and returns a list of connections.
    """
    connections = []
    for connection in data:
        source = connection['source']
        target = connection['target']
        connections.append((source, target))
    return connections