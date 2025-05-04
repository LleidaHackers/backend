
from abc import abstractmethod
from dataclasses import dataclass
import random
from threading import Thread
import time
from typing import List
from paho.mqtt import client as mqtt_client
from Connection import Connection


class BaseModule(Thread):
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

  connectedIn: list[str] # List of ids of connected modules
  connectedOut: list[str] # List of ids of connected modules


  def __init__(self, name):

    super().__init__(daemon=True)     
    self.id = random.randint(0, 1000000)  # Random ID for the module
    self.name = name
    self.posX = 0
    self.posY = 0 
    self.client_id = f'publish-{random.randint(0, 1000)}'
    self.conn_inputs : List[Connection]= []
    self.conn_outputs : List[Connection]= [] 
    self.current_outputs : dict
    self.current_inputs : dict
    self.running = False
    self.connectedIn = []
    self.connectedOut = []
    @abstractmethod
    def in_out_map(self, input_type: str) -> str:
        """All child classes must implement this"""
        pass
      
    @abstractmethod
    def update_outputs(self, input_type: str) -> str:
        """All child classes must implement this"""
        pass
  
     
  
  
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
  
  def run(self):
        self.running = True
        client = self.connect_mqtt()
        client.loop_start()
        outputs = list(self.current_outputs.keys())
        topics = [] #[(f"/{self.conn_inputs[0].type}/{self.conn_inputs[0].id}",0),(f"/{self.conn_inputs[1].type}/{self.conn_inputs[1].id}",0),("Server3/kpi3",0)]
        for connection in self.conn_inputs:
          topics.append((f"/{connection.type}/{connection.id}",0))
        
        self.subscribe_child(client,topics)
        while self.running:
          for output in outputs:
            #print(f"on pub->{self.current_outputs}")
            self.publish(client,f"/{output}/{self.id}",self.current_outputs[output],self.__module__ )
            
          time.sleep(1)
            
        client.loop_stop()

  def stop(self):
      """Stop the simulation thread."""
      
      self.running = False
  def subscribe(self,client: mqtt_client,topic):
    def on_message(client, userdata, msg):
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")
        
    client.subscribe(topic)
    client.on_message = on_message
    #client.on_message = on_message
  
  def subscribe_child(self, client: mqtt_client, topic):
    # First call parent's implementation
      #print(f"AAAAAAAAAAAAAA{topic}")
      self.subscribe(client, topic)
      #print(f"server:{self.id} topcis:{topic}")
      def child_on_message(client, userdata, msg):
          #print(f"[{self.__module__ }-{self.id}]Recieved: {msg.payload.decode()} from {msg.topic}")
          #print(str(msg.topic).split("/")[1])
          #self.current_outputs[in_out_map(str(topic).split("/")[1])] = msg.payload.decode()
          self.current_inputs[str(msg.topic).split("/")[1]] = msg.payload.decode()
         
          self.update_outputs()
          #print(f"aaaaa {self.current_outputs[in_out_map(str(topic).split("/")[1])]}")
      client.on_message = child_on_message    
  
  
  def publish(self,client,topic,msg,name=""):
      result = client.publish(topic, msg)
      # result: [0, 1]
      status = result[0]
      # if status == 0:
          #print(f"[{self.__module__}-{self.id}]Send: `{msg}` to topic `{topic}`")
      #else:
      #    print(f"Failed to send message to topic {topic}")

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

