import json
from utils import parseModule

if __name__ == "__main__":
    parsedObjects = []
    with open("data2.json", "r") as file:
        data = json.load(file)
        for node in data[0].get("nodes"):
            parsedObjects.append(parseModule(node))

        edges = data[0].get("edges")
        for obj in parsedObjects:
            for edge in edges:
                if obj.id == edge.get("source") and edge.get("target") not in obj.connectedOut:
                    obj.connectedOut.append(edge.get("target"))
                elif obj.id == edge.get("target") and edge.get("source") not in obj.connectedIn:
                    obj.connectedIn.append(edge.get("source"))

        for obj in parsedObjects:
            print(f"ID: {obj.id}, Name: {obj.name}, Connected In: {obj.connectedIn}, Connected Out: {obj.connectedOut}")