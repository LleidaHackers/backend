class Transformer:
    def __init__(self):
        self.id = 1
        self.name = "Transformer_100"
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