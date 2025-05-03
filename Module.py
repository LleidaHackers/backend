class Module:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.conns = {
            "inputs" : [],
            "outputs" : []
        }
        
class Connection:
    def __init__(self, id, type, amount, dev_id):
        self.id = id
        self.type = type
        self.amount = amount
        self.dev_id = dev_id
