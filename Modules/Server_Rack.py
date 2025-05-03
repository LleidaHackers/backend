class Server_Rack:
    def __init__(self):
        self.id = 13
        self.name = "Server_Rack_100"
        self.properties = {
            'inputs': {
                "Usable_Power": 75,
                "Chilled_Water": 15,
                "Internal_Network": 10,
                "Space_X": 40,
                "Space_Y": 40,
                "Price": 8000
            },
            'outputs': {
                "Distilled_Water": 15,
                "Processing": 100,
                "External Network": 100
            }
        }
        self.current = {
            'inputs': {
                "Usable_Power": 0,
                "Chilled_Water": 0,
                "Internal_Network": 0,
            },
            'outputs': {
                "Distilled_Water": 0,
                "Processing": 0,
                "External Network": 0
            }
        }