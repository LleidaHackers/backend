from Module import Module
class Transformer(Module):
    def __init__(self,name,id):
        super().__init__(name, id)
        self.properties = {
            'inputs': {
                "Grid_Connection": 1,
                "Space_X": 40,
                "Space_Y": 45,
                "Price": 1000
            },
            'outputs': {
                "Usable_Power": 100
            }
        }
        self.current = {
            'inputs': {
                "Grid_Connection": 0,
            },
            'outputs': {
                "Usable_Power": 0
            }
        }