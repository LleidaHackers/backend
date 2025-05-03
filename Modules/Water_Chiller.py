class Water_Chiller:
    def __init__(self):
        self.id = 8
        self.name = "Water_Chiller_100"
        self.properties = {
            'inputs': {
                "Distlled_Water": 100,
                "Usable_Power": 500,
                "Space_X": 100,
                "Space_Y": 100,
                "Price": 40000
            },
            'outputs': {
                "Chilled_Water": 95
            }
        }
        self.current = {
            'inputs': {
                "Distlled_Water": 0,
                "Usable_Power": 0,
            },
            'outputs': {
                "Chilled_Water": 0
            }
        }