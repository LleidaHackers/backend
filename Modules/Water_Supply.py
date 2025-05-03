class Water_Supply:
    def __init__(self):
        self.id = 4
        self.name = "Water_Supply_100"
        self.properties = {
            'inputs': {
                "Water_Connection": 1,
                "Space_X": 50,
                "Space_Y": 50,
                "Price": 200
            },
            'outputs': {
                "Fresh_Water": 100
            }
        }
        self.current = {
            'inputs': {
                "Water_Connection": 0,
            },
            'outputs': {
                "Fresh_Water": 0
            }
        }