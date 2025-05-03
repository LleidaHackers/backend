class Network_Rack:
    def __init__(self):
        self.id = 10
        self.name = "Network_Rack_50"
        self.properties = {
            'inputs': {
                "Usable_Power": 50,
                "Chilled_Water": 5,
                "Space_X": 40,
                "Space_Y": 40,
                "Price": 2000
            },
            'outputs': {
                "Internal_Network": 50,
                "Fresh_Water": 5
            }
        }
        self.current = {
            'inputs': {
                "Usable_Power": 0,
                "Chilled_Water": 0,
            },
            'outputs': {
                "Internal_Network": 0,
                "Fresh_Water": 0
            }
        }