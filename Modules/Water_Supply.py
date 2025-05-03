from module import Module
class Water_Supply(Module):
    def __init__(self,name,id):
        super().__init__(name, id)
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