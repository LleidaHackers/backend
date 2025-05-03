
class Water_Treatment:
    def __init__(self):
        self.id = 5
        self.name = "Water_Treatment_50"
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
