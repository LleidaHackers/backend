from dataclasses import dataclass
import random
import time
from typing import List
from paho.mqtt import client as mqtt_client
from Connection import Connection


class BaseModule:
  broker = 'localhost'
  port = 1883
  # Generate a Client ID with the publish prefix.

  id: int
  name: str
  # Position, will vary in the future (after solving for positioning)
  posX: int
  posY: int
  # Characteristics, stay the same, will be set when
  sizeX: int
  sizeY: int
  price: int
  # Connection with other modules
  connections: dict 


  def __init__(self, name):
    self.id = random.randint(0, 1000000)  # Random ID for the module
    self.name = name
    self.posX = 0
    self.posY = 0 
    self.client_id = f'publish-{random.randint(0, 1000)}'
    self.conn_inputs : List[Connection]= []
    self.conn_outputs : List[Connection]= [] 


  def connect_mqtt(self):
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print(f"Failed to connect, return code {rc}")

    # Ensure only one callback_api_version is passed
    client = mqtt_client.Client(
        client_id=self.client_id,  # Make sure self.client_id is just a string
        callback_api_version=mqtt_client.CallbackAPIVersion.VERSION1  # or VERSION2
    )
    
    # client.username_pw_set(username, password)  # Uncomment if auth is needed
    client.on_connect = on_connect
    
    error = client.connect(self.broker, self.port)
    print(error)
    return client
  
  def subscribe(self,client: mqtt_client,topic):
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

    client.subscribe(topic)
    client.on_message = on_message
    #client.on_message = on_message
  def publish(self,client,topic,msg):
      result = client.publish(topic, msg)
      # result: [0, 1]
      status = result[0]
      if status == 0:
          print(f"Send `{msg}` to topic `{topic}`")
      else:
          print(f"Failed to send message to topic {topic}")


  def setInput(self, other_object_id):
    if other_object_id in self.connections['input']:
      print(f"Input connection with ID {other_object_id} already exists.")
    else:
      self.connections['input'].append(other_object_id)


  def setOutput(self, other_object_id):
    if other_object_id in self.connections['output']:
      print(f"Output connection with ID {other_object_id} already exists.")
    else:
      self.connections['output'].append(other_object_id)


  def removeInput(self, other_object_id):
    if other_object_id in self.connections['input']:
      self.connections['input'].remove(other_object_id)
    else:
      print(f"Input connection with ID {other_object_id} not found for removal.")


  def removeOutput(self, other_object_id):
    if other_object_id in self.connections['output']:
      self.connections['output'].remove(other_object_id)
    else:
      print(f"output connection with ID {other_object_id} not found for removal.")