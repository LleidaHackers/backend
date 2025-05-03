class Module:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.posX = 0
        self.posY = 0
        self.conns = {
            "inputs": [],
            "outputs": []
        }
  
    def add_input_connection(self, connection):
        self.conns["inputs"].append(connection)
    
    def add_output_connection(self, connection):
        self.conns["outputs"].append(connection)
 
 
class Connection:
    def __init__(self, id, type, amount, dev_id):
        self.id = id
        self.type = type
        self.amount = amount
        self.dev_id = dev_id
