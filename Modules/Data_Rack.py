from Module import Module

class Data_Rack(Module):
    def __init__(self, name, id):
        super().__init__(name, id)

        self.properties = {
            'inputs': {
                "Usable_Power": 15,
                "Chilled_Water": 3,
                "Internal_Network": 5,
                "Space_X": 40,
                "Space_Y": 40,
                "Price": 2000
            },
            'outputs': {
                "Distilled_Water": 3,
                "Data_Storage": 100
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
                "Data_Storage": 0
            }
        }
