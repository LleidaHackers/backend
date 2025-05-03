from module import Module
class Water_Treatment(Module):
    def __init__(self,name,id):
        super().__init__(name, id)
        self.properties = {
            'inputs': {
                "Fresh_Water": 50,
                "Usable_Power": 50,
                "Space_X": 50,
                "Space_Y": 50,
                "Price": 10000
            },
            'outputs': {
                "Distlled_Water": 50
            }
        }
        self.current = {
            'inputs': {
                "Fresh_Water": 0,
                "Usable_Power": 0,
            },
            'outputs': {
                "Distlled_Water": 0
            }
        }
