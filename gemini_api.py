from google import genai
import os
import requests
from dotenv import load_dotenv
import json
from pymongo import MongoClient
# Abrir y leer el archivo JSON
with open("data/devices.json", "r") as file:
    total = json.load(file)
# Cargar variables de entorno desde .env
load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=API_KEY)

context = """You are a helpful assistant. Your task is to help design a data center.
The data center should be designed to be energy efficient, scalable, and secure, and have the less costs possible.
The data center is formed by a set of different components, which are, in JSON format:
"""

total="""
[
    {
      "name": "Transformer_100",
      "icon": "Zap",
      "cost": 1000,
      "surface": 1800,
      "energyConsumption": 0,
      "energyProduction": 100,
      "waterUsage": 0,
      "waterProduction": 0,
      "chilledWaterUsage": 0,
      "chilledWaterProduction": 0,
      "freshWaterUsage": 0,
      "freshWaterProduction": 0,
      "distilledWaterUsage": 0,
      "distilledWaterProduction": 0,
      "internalNetworkUsage": 0,
      "internalNetworkProduction": 0,
      "externalNetworkProduction": 0,
      "soundLevel": 0,
      "procesProduction": 0,
      "dataStorageProduction": 0,
      "dataStorageUsage": 0,
      "procesUsage": 0,
      "gridConnectionOffer": 0,
      "waterConnectionOffer": 0,
      "gridConnectionUsage": 1,
      "waterConnectionUsage": 0,
      "inputs": [
        "Grid_Connection"
      ],
      "outputs": [
        "Usable_Power"
      ],
      "type": "transformer"
    },
    {
      "name": "Transformer_1000",
      "icon": "Zap",
      "cost": 50000,
      "surface": 10000,
      "energyConsumption": 0,
      "energyProduction": 1000,
      "waterUsage": 0,
      "waterProduction": 0,
      "chilledWaterUsage": 0,
      "chilledWaterProduction": 0,
      "freshWaterUsage": 0,
      "freshWaterProduction": 0,
      "distilledWaterUsage": 0,
      "distilledWaterProduction": 0,
      "internalNetworkUsage": 0,
      "internalNetworkProduction": 0,
      "externalNetworkProduction": 0,
      "soundLevel": 0,
      "procesProduction": 0,
      "dataStorageProduction": 0,
      "dataStorageUsage": 0,
      "procesUsage": 0,
      "gridConnectionOffer": 0,
      "waterConnectionOffer": 0,
      "gridConnectionUsage": 1,
      "waterConnectionUsage": 0,
      "inputs": [
        "Grid_Connection"
      ],
      "outputs": [
        "Usable_Power"
      ],
      "type": "transformer"
    },
    {
      "name": "Transformer_5000",
      "icon": "Zap",
      "cost": 250000,
      "surface": 40000,
      "energyConsumption": 0,
      "energyProduction": 5000,
      "waterUsage": 0,
      "waterProduction": 0,
      "chilledWaterUsage": 0,
      "chilledWaterProduction": 0,
      "distilledWaterUsage": 0,
      "distilledWaterProduction": 0,
      "internalNetworkUsage": 0,
      "internalNetworkProduction": 0,
      "externalNetworkProduction": 0,
      "soundLevel": 0,
      "procesProduction": 0,
      "dataStorageProduction": 0,
      "dataStorageUsage": 0,
      "procesUsage": 0,
      "gridConnectionOffer": 0,
      "waterConnectionOffer": 0,
      "gridConnectionUsage": 1,
      "waterConnectionUsage": 0,
      "inputs": [
        "Grid_Connection"
      ],
      "outputs": [
        "Usable_Power"
      ],
      "type": "transformer"
    }
  ],
  "water_supplies": [
    {
      "name": "Water_Supply_100",
      "icon": "Droplet",
      "cost": 200,
      "surface": 2500,
      "energyConsumption": 0,
      "energyProduction": 0,
      "waterUsage": 0,
      "waterProduction": 0,
      "chilledWaterUsage": 0,
      "chilledWaterProduction": 0,
      "freshWaterUsage": 0,
      "freshWaterProduction": 100,
      "distilledWaterUsage": 0,
      "distilledWaterProduction": 0,
      "internalNetworkUsage": 0,
      "internalNetworkProduction": 0,
      "externalNetworkProduction": 0,
      "soundLevel": 0,
      "procesProduction": 0,
      "dataStorageProduction": 0,
      "dataStorageUsage": 0,
      "procesUsage": 0,
      "gridConnectionOffer": 0,
      "waterConnectionOffer": 0,
      "gridConnectionUsage": 0,
      "waterConnectionUsage": 1,
      "inputs": [
        "Water_Connection"
      ],
      "outputs": [
        "Fresh_Water"
      ],
      "type": "water_supply"
    },
    {
      "name": "Water_Supply_500",
      "icon": "Droplet",
      "cost": 400,
      "surface": 15000,
      "energyConsumption": 0,
      "energyProduction": 0,
      "waterUsage": 0,
      "waterProduction": 0,
      "chilledWaterUsage": 0,
      "chilledWaterProduction": 0,
      "freshWaterUsage": 0,
      "freshWaterProduction": 500,
      "distilledWaterUsage": 0,
      "distilledWaterProduction": 0,
      "internalNetworkUsage": 0,
      "internalNetworkProduction": 0,
      "externalNetworkProduction": 0,
      "soundLevel": 0,
      "procesProduction": 0,
      "dataStorageProduction": 0,
      "dataStorageUsage": 0,
      "procesUsage": 0,
      "gridConnectionOffer": 0,
      "waterConnectionOffer": 0,
      "gridConnectionUsage": 0,
      "waterConnectionUsage": 1,
      "inputs": [
        "Water_Connection"
      ],
      "outputs": [
        "Fresh_Water"
      ],
      "type": "water_supply"
    }
  ],
  "water_treatments": [
    {
      "name": "Water_Treatment_50",
      "icon": "Cross",
      "cost": 10000,
      "surface": 2500,
      "energyConsumption": 50,
      "energyProduction": 0,
      "waterUsage": 0,
      "waterProduction": 0,
      "chilledWaterUsage": 0,
      "chilledWaterProduction": 0,
      "freshWaterUsage": 50,
      "freshWaterProduction": 0,
      "distilledWaterUsage": 0,
      "distilledWaterProduction": 50,
      "internalNetworkUsage": 0,
      "internalNetworkProduction": 0,
      "externalNetworkProduction": 0,
      "soundLevel": 0,
      "procesProduction": 0,
      "dataStorageProduction": 0,
      "dataStorageUsage": 0,
      "procesUsage": 0,
      "gridConnectionOffer": 0,
      "waterConnectionOffer": 0,
      "gridConnectionUsage": 0,
      "waterConnectionUsage": 0,
      "inputs": [
        "Fresh_Water",
        "Usable_Power"
      ],
      "outputs": [
        "Distilled_Water"
      ],
      "type": "water_treatment"
    },
    {
      "name": "Water_Treatment_250",
      "icon": "Cross",
      "cost": 40000,
      "surface": 40000,
      "energyConsumption": 90,
      "energyProduction": 0,
      "waterUsage": 0,
      "waterProduction": 0,
      "chilledWaterUsage": 0,
      "chilledWaterProduction": 0,
      "freshWaterUsage": 250,
      "freshWaterProduction": 0,
      "distilledWaterUsage": 0,
      "distilledWaterProduction": 250,
      "internalNetworkUsage": 0,
      "internalNetworkProduction": 0,
      "externalNetworkProduction": 0,
      "soundLevel": 0,
      "procesProduction": 0,
      "dataStorageProduction": 0,
      "dataStorageUsage": 0,
      "procesUsage": 0,
      "gridConnectionOffer": 0,
      "waterConnectionOffer": 0,
      "gridConnectionUsage": 0,
      "waterConnectionUsage": 0,
      "inputs": [
        "Fresh_Water",
        "Usable_Power"
      ],
      "outputs": [
        "Distilled_Water"
      ],
      "type": "water_treatment"
    },
    {
      "name": "Water_Treatment_500",
      "icon": "Cross",
      "cost": 70000,
      "surface": 160000,
      "energyConsumption": 150,
      "energyProduction": 0,
      "waterUsage": 500,
      "waterProduction": 0,
      "chilledWaterUsage": 0,
      "chilledWaterProduction": 0,
      "freshWaterUsage": 500,
      "freshWaterProduction": 0,
      "distilledWaterUsage": 0,
      "distilledWaterProduction": 500,
      "internalNetworkUsage": 0,
      "internalNetworkProduction": 0,
      "externalNetworkProduction": 0,
      "soundLevel": 0,
      "procesProduction": 0,
      "dataStorageProduction": 0,
      "dataStorageUsage": 0,
      "procesUsage": 0,
      "gridConnectionOffer": 0,
      "waterConnectionOffer": 0,
      "gridConnectionUsage": 0,
      "waterConnectionUsage": 0,
      "inputs": [
        "Fresh_Water",
        "Usable_Power"
      ],
      "outputs": [
        "Distilled_Water"
      ],
      "type": "water_treatment"
    }
  ],
  "water_chillers": [
    {
      "name": "Water_Chiller_100",
      "icon": "Snowflake",
      "cost": 40000,
      "surface": 10000,
      "energyConsumption": 500,
      "energyProduction": 0,
      "waterUsage": 0,
      "waterProduction": 0,
      "chilledWaterUsage": 0,
      "chilledWaterProduction": 95,
      "freshWaterUsage": 0,
      "freshWaterProduction": 0,
      "distilledWaterUsage": 100,
      "distilledWaterProduction": 0,
      "internalNetworkUsage": 0,
      "internalNetworkProduction": 0,
      "externalNetworkProduction": 0,
      "soundLevel": 0,
      "procesProduction": 0,
      "dataStorageProduction": 0,
      "dataStorageUsage": 0,
      "procesUsage": 0,
      "gridConnectionOffer": 0,
      "waterConnectionOffer": 0,
      "gridConnectionUsage": 0,
      "waterConnectionUsage": 0,
      "inputs": [
        "Distilled_Water",
        "Usable_Power"
      ],
      "outputs": [
        "Chilled_Water"
      ],
      "type": "water_chiller"
    },
    {
      "name": "Water_Chiller_400",
      "icon": "Snowflake",
      "cost": 150000,
      "surface": 30000,
      "energyConsumption": 1500,
      "energyProduction": 0,
      "waterUsage": 0,
      "waterProduction": 0,
      "chilledWaterUsage": 0,
      "chilledWaterProduction": 390,
      "freshWaterUsage": 0,
      "freshWaterProduction": 0,
      "distilledWaterUsage": 400,
      "distilledWaterProduction": 0,
      "internalNetworkUsage": 0,
      "internalNetworkProduction": 0,
      "externalNetworkProduction": 0,
      "soundLevel": 0,
      "procesProduction": 0,
      "dataStorageProduction": 0,
      "dataStorageUsage": 0,
      "procesUsage": 0,
      "gridConnectionOffer": 0,
      "waterConnectionOffer": 0,
      "gridConnectionUsage": 0,
      "waterConnectionUsage": 0,
      "inputs": [
        "Distilled_Water",
        "Usable_Power"
      ],
      "outputs": [
        "Chilled_Water"
      ],
      "type": "water_chiller"
    }
  ],
  "network_racks": [
    {
      "name": "Network_Rack_50",
      "icon": "EthernetPort",
      "cost": 2000,
      "surface": 1600,
      "energyConsumption": 50,
      "energyProduction": 0,
      "waterUsage": 0,
      "waterProduction": 0,
      "chilledWaterUsage": 5,
      "chilledWaterProduction": 0,
      "freshWaterUsage": 0,
      "freshWaterProduction": 5,
      "distilledWaterUsage": 0,
      "distilledWaterProduction": 0,
      "internalNetworkUsage": 0,
      "internalNetworkProduction": 50,
      "externalNetworkProduction": 0,
      "soundLevel": 0,
      "procesProduction": 0,
      "dataStorageProduction": 0,
      "dataStorageUsage": 0,
      "procesUsage": 0,
      "gridConnectionOffer": 0,
      "waterConnectionOffer": 0,
      "gridConnectionUsage": 0,
      "waterConnectionUsage": 0,
      "inputs": [
        "Usable_Power",
        "Chilled_Water"
      ],
      "outputs": [
        "Internal_Network",
        "Fresh_Water"
      ],
      "type": "network_rack"
    },
    {
      "name": "Network_Rack_100",
      "icon": "EthernetPort",
      "cost": 8000,
      "surface": 1600,
      "energyConsumption": 75,
      "energyProduction": 0,
      "waterUsage": 0,
      "waterProduction": 0,
      "chilledWaterUsage": 7,
      "chilledWaterProduction": 0,
      "freshWaterUsage": 0,
      "freshWaterProduction": 7,
      "distilledWaterUsage": 0,
      "distilledWaterProduction": 0,
      "internalNetworkUsage": 0,
      "internalNetworkProduction": 100,
      "externalNetworkProduction": 0,
      "soundLevel": 0,
      "procesProduction": 0,
      "dataStorageProduction": 0,
      "dataStorageUsage": 0,
      "procesUsage": 0,
      "gridConnectionOffer": 0,
      "waterConnectionOffer": 0,
      "gridConnectionUsage": 0,
      "waterConnectionUsage": 0,
      "inputs": [
        "Usable_Power",
        "Chilled_Water"
      ],
      "outputs": [
        "Internal_Network",
        "Fresh_Water"
      ],
      "type": "network_rack"
    },
    {
      "name": "Network_Rack_200",
      "icon": "EthernetPort",
      "cost": 20000,
      "surface": 1600,
      "energyConsumption": 95,
      "energyProduction": 0,
      "waterUsage": 0,
      "waterProduction": 0,
      "chilledWaterUsage": 10,
      "chilledWaterProduction": 0,
      "freshWaterUsage": 0,
      "freshWaterProduction": 10,
      "distilledWaterUsage": 0,
      "distilledWaterProduction": 0,
      "internalNetworkUsage": 0,
      "internalNetworkProduction": 200,
      "externalNetworkProduction": 0,
      "soundLevel": 0,
      "procesProduction": 0,
      "dataStorageProduction": 0,
      "dataStorageUsage": 0,
      "procesUsage": 0,
      "gridConnectionOffer": 0,
      "waterConnectionOffer": 0,
      "gridConnectionUsage": 0,
      "waterConnectionUsage": 0,
      "inputs": [
        "Usable_Power",
        "Chilled_Water"
      ],
      "outputs": [
        "Internal_Network",
        "Fresh_Water"
      ],
      "type": "network_rack"
    }
  ],
  "server_racks": [
    {
      "name": "Server_Rack_100",
      "icon": "Wifi",
      "cost": 8000,
      "surface": 1600,
      "energyConsumption": 75,
      "energyProduction": 0,
      "waterUsage": 0,
      "waterProduction": 0,
      "chilledWaterUsage": 15,
      "chilledWaterProduction": 0,
      "freshWaterUsage": 0,
      "freshWaterProduction": 5,
      "distilledWaterUsage": 0,
      "distilledWaterProduction": 15,
      "internalNetworkUsage": 10,
      "internalNetworkProduction": 0,
      "externalNetworkProduction": 100,
      "soundLevel": 0,
      "procesProduction": 100,
      "dataStorageProduction": 0,
      "dataStorageUsage": 0,
      "procesUsage": 0,
      "gridConnectionOffer": 0,
      "waterConnectionOffer": 0,
      "gridConnectionUsage": 0,
      "waterConnectionUsage": 0,
      "inputs": [
        "Usable_Power",
        "Chilled_Water",
        "Internal_Network"
      ],
      "outputs": [
        "External_Network",
        "Processing"
      ],
      "type": "server_rack"
    },
    {
      "name": "Server_Rack_200",
      "icon": "Wifi",
      "cost": 12000,
      "surface": 1600,
      "energyConsumption": 125,
      "energyProduction": 0,
      "waterUsage": 0,
      "waterProduction": 0,
      "chilledWaterUsage": 25,
      "chilledWaterProduction": 0,
      "freshWaterUsage": 0,
      "freshWaterProduction": 10,
      "distilledWaterUsage": 0,
      "distilledWaterProduction": 25,
      "internalNetworkUsage": 18,
      "internalNetworkProduction": 0,
      "externalNetworkProduction": 150,
      "soundLevel": 0,
      "procesProduction": 200,
      "dataStorageProduction": 0,
      "dataStorageUsage": 0,
      "procesUsage": 0,
      "gridConnectionOffer": 0,
      "waterConnectionOffer": 0,
      "gridConnectionUsage": 0,
      "waterConnectionUsage": 0,
      "inputs": [
        "Usable_Power",
        "Chilled_Water",
        "Internal_Network"
      ],
      "outputs": [
        "External_Network",
        "Processing"
      ],
      "type": "server_rack"
    },
    {
      "name": "Server_Rack_500",
      "icon": "Wifi",
      "cost": 50000,
      "surface": 1600,
      "energyConsumption": 240,
      "energyProduction": 0,
      "waterUsage": 0,
      "waterProduction": 0,
      "chilledWaterUsage": 50,
      "chilledWaterProduction": 0,
      "freshWaterUsage": 0,
      "freshWaterProduction": 20,
      "distilledWaterUsage": 0,
      "distilledWaterProduction": 50,
      "internalNetworkUsage": 32,
      "internalNetworkProduction": 0,
      "externalNetworkProduction": 400,
      "soundLevel": 0,
      "procesProduction": 1000,
      "dataStorageProduction": 0,
      "dataStorageUsage": 0,
      "procesUsage": 0,
      "gridConnectionOffer": 0,
      "waterConnectionOffer": 0,
      "gridConnectionUsage": 0,
      "waterConnectionUsage": 0,
      "inputs": [
        "Usable_Power",
        "Chilled_Water",
        "Internal_Network"
      ],
      "outputs": [
        "External_Network",
        "Processing"
      ],
      "type": "server_rack"
    }
  ],
  "data_racks": [
    {
      "name": "Data_Rack_100",
      "icon": "HardDriveDownload",
      "cost": 2000,
      "surface": 1600,
      "energyConsumption": 15,
      "energyProduction": 0,
      "waterUsage": 0,
      "waterProduction": 0,
      "chilledWaterUsage": 3,
      "chilledWaterProduction": 0,
      "freshWaterUsage": 0,
      "freshWaterProduction": 0,
      "distilledWaterUsage": 0,
      "distilledWaterProduction": 3,
      "internalNetworkUsage": 5,
      "internalNetworkProduction": 0,
      "externalNetworkProduction": 0,
      "soundLevel": 0,
      "procesProduction": 0,
      "dataStorageProduction": 100,
      "dataStorageUsage": 0,
      "procesUsage": 0,
      "gridConnectionOffer": 0,
      "waterConnectionOffer": 0,
      "gridConnectionUsage": 0,
      "waterConnectionUsage": 0,
      "inputs": [
        "Usable_Power",
        "Chilled_Water",
        "Internal_Network"
      ],
      "outputs": [
        "Data_Storage"
      ],
      "type": "data_rack"
    },
    {
      "name": "Data_Rack_250",
      "icon": "HardDriveDownload",
      "cost": 7500,
      "surface": 1600,
      "energyConsumption": 25,
      "energyProduction": 0,
      "waterUsage": 0,
      "waterProduction": 0,
      "chilledWaterUsage": 3,
      "chilledWaterProduction": 0,
      "freshWaterUsage": 0,
      "freshWaterProduction": 0,
      "distilledWaterUsage": 0,
      "distilledWaterProduction": 3,
      "internalNetworkUsage": 10,
      "internalNetworkProduction": 0,
      "externalNetworkProduction": 0,
      "soundLevel": 0,
      "procesProduction": 0,
      "dataStorageProduction": 250,
      "dataStorageUsage": 0,
      "procesUsage": 0,
      "gridConnectionOffer": 0,
      "waterConnectionOffer": 0,
      "gridConnectionUsage": 0,
      "waterConnectionUsage": 0,
      "inputs": [
        "Usable_Power",
        "Chilled_Water",
        "Internal_Network"
      ],
      "outputs": [
        "Data_Storage"
      ],
      "type": "data_rack"
    },
    {
      "name": "Data_Rack_500",
      "icon": "HardDriveDownload",
      "cost": 20500,
      "surface": 1600,
      "energyConsumption": 40,
      "energyProduction": 0,
      "waterUsage": 0,
      "waterProduction": 0,
      "chilledWaterUsage": 6,
      "chilledWaterProduction": 0,
      "freshWaterUsage": 0,
      "freshWaterProduction": 0,
      "distilledWaterUsage": 0,
      "distilledWaterProduction": 6,
      "internalNetworkUsage": 20,
      "internalNetworkProduction": 0,
      "externalNetworkProduction": 0,
      "soundLevel": 0,
      "procesProduction": 0,
      "dataStorageProduction": 500,
      "dataStorageUsage": 0,
      "procesUsage": 0,
      "gridConnectionOffer": 0,
      "waterConnectionOffer": 0,
      "gridConnectionUsage": 0,
      "waterConnectionUsage": 0,
      "inputs": [
        "Usable_Power",
        "Chilled_Water",
        "Internal_Network"
      ],
      "outputs": [
        "Data_Storage"
      ],
      "type": "data_rack"
    }
  ],
  "data_center": [
    {
      "name": "Server_Square",
      "icon": "DatabaseZap",
      "cost": 1000000,
      "surface": 500,
      "energyConsumption": 0,
      "energyProduction": 0,
      "waterUsage": 0,
      "waterProduction": 0,
      "chilledWaterUsage": 0,
      "chilledWaterProduction": 0,
      "freshWaterUsage": 0,
      "freshWaterProduction": 0,
      "distilledWaterUsage": 0,
      "distilledWaterProduction": 0,
      "internalNetworkUsage": 0,
      "internalNetworkProduction": 0,
      "externalNetworkProduction": 0,
      "soundLevel": 0,
      "procesProduction": 0,
      "dataStorageProduction": 0,
      "dataStorageUsage": 1000,
      "procesUsage": 1000,
      "gridConnectionOffer": 3,
      "waterConnectionOffer": 1,
      "gridConnectionUsage": 0,
      "waterConnectionUsage": 0,
      "inputs": [
        "Data_Storage",
        "External_Network",
        "Processing"
      ],
      "outputs": [
        "Grid_Connection",
        "Water_Connection"
      ],
      "type": "data_center"
    },
    {
      "name": "Dense_Storage",
      "icon": "Database",
      "cost": 5000000,
      "surface": 0,
      "energyConsumption": 0,
      "energyProduction": 0,
      "waterUsage": 0,
      "waterProduction": 0,
      "chilledWaterUsage": 0,
      "chilledWaterProduction": 0,
      "freshWaterUsage": 0,
      "freshWaterProduction": 0,
      "distilledWaterUsage": 0,
      "distilledWaterProduction": 0,
      "internalNetworkUsage": 0,
      "internalNetworkProduction": 0,
      "externalNetworkProduction": 0,
      "soundLevel": 0,
      "procesProduction": 0,
      "dataStorageProduction": 0,
      "dataStorageUsage": 0,
      "procesUsage": 0,
      "gridConnectionOffer": 1000,
      "waterConnectionOffer": 1000,
      "gridConnectionUsage": 0,
      "waterConnectionUsage": 0,
      "inputs": [
        "Data_Storage",
        "Processing"
      ],
      "outputs": [
        "Grid_Connection",
        "Water_Connection"
      ],
      "type": "data_center"
    },
    {
      "name": "Supercomputer",
      "icon": "HardDrive",
      "cost": 10000000,
      "surface": 2000000,
      "energyConsumption": 0,
      "energyProduction": 0,
      "waterUsage": 0,
      "waterProduction": 0,
      "chilledWaterUsage": 0,
      "chilledWaterProduction": 0,
      "freshWaterUsage": 0,
      "freshWaterProduction": 0,
      "distilledWaterUsage": 0,
      "distilledWaterProduction": 0,
      "internalNetworkUsage": 0,
      "internalNetworkProduction": 0,
      "externalNetworkProduction": 0,
      "soundLevel": 0,
      "procesProduction": 0,
      "dataStorageProduction": 0,
      "dataStorageUsage": 0,
      "procesUsage": 0,
      "gridConnectionOffer": 1000,
      "waterConnectionOffer": 1000,
      "gridConnectionUsage": 0,
      "waterConnectionUsage": 0,
      "inputs": [
        "Usable_Power",
        "Processing"
      ],
      "outputs": [
        "Grid_Connection",
        "Water_Connection"
      ],
      "type": "data_center"
    }
  ]


Right now, the current configuration is:
"nodes": [
    {
      "id": "water_supply_500-2",
      "type": "custom",
      "position": {
        "x": 115.84438232598632,
        "y": 374.8674355494695
      },
      "data": {
        "label": "Water_Supply_500\n($400)",
        "type": "water_supply",
        "power": 0,
        "demand": 0,
        "inputs": [
          "Water_Connection"
        ],
        "outputs": [
          "Fresh_Water"
        ],
        "surface": 15000
      },
      "style": {
        "borderRadius": 8,
        "padding": 8,
        "backgroundColor": "#D1FAE5",
        "border": "1px solid #CBD5E1"
      },
      "width": 177,
      "height": 111
    },
    {
      "id": "water_treatment_250-3",
      "type": "custom",
      "position": {
        "x": 361.6153169873188,
        "y": 367.38515164136356
      },
      "data": {
        "label": "Water_Treatment_250\n($40000)",
        "type": "water_treatment",
        "power": 0,
        "demand": 90,
        "inputs": [
          "Fresh_Water",
          "Usable_Power"
        ],
        "outputs": [
          "Distilled_Water"
        ],
        "surface": 40000
      },
      "style": {
        "borderRadius": 8,
        "padding": 8,
        "backgroundColor": "#D1FAE5",
        "border": "1px solid #CBD5E1"
      },
      "width": 195,
      "height": 111
    },
    {
      "id": "water_chiller_400-4",
      "type": "custom",
      "position": {
        "x": 669.746427371424,
        "y": 330.74746339513666
      },
      "data": {
        "label": "Water_Chiller_400\n($150000)",
        "type": "water_chiller",
        "power": 0,
        "demand": 1500,
        "inputs": [
          "Distilled_Water",
          "Usable_Power"
        ],
        "outputs": [
          "Chilled_Water"
        ],
        "surface": 30000
      },
      "style": {
        "borderRadius": 8,
        "padding": 8,
        "backgroundColor": "#D1FAE5",
        "border": "1px solid #CBD5E1"
      },
      "width": 177,
      "height": 111
    },
    {
      "id": "server_rack_500-5",
      "type": "custom",
      "position": {
        "x": 590.1692458384101,
        "y": 124.583328314326
      },
      "data": {
        "label": "Server_Rack_500\n($50000)",
        "type": "server_rack",
        "power": 0,
        "demand": 240,
        "inputs": [
          "Usable_Power",
          "Chilled_Water",
          "Internal_Network"
        ],
        "outputs": [
          "External_Network",
          "Processing"
        ],
        "surface": 1600
      },
      "style": {
        "borderRadius": 8,
        "padding": 8,
        "backgroundColor": "#E5E7EB",
        "border": "1px solid #CBD5E1"
      },
      "width": 177,
      "height": 111
    },
    {
      "id": "server_square-6",
      "type": "custom",
      "position": {
        "x": 567.0447638986149,
        "y": -64.92234356483911
      },
      "data": {
        "label": "Server_Square\n($1000000)",
        "type": "data_center",
        "power": 0,
        "demand": 0,
        "inputs": [
          "Data_Storage",
          "External_Network",
          "Processing"
        ],
        "outputs": [
          "Grid_Connection",
          "Water_Connection"
        ],
        "surface": 500
      },
      "style": {
        "borderRadius": 8,
        "padding": 8,
        "backgroundColor": "#D1FAE5",
        "border": "1px solid #CBD5E1"
      },
      "width": 177,
      "height": 111
    },
    {
      "id": "data_rack_500-7",
      "type": "custom",
      "position": {
        "x": 964.4107951194167,
        "y": 75.6221857528086
      },
      "data": {
        "label": "Data_Rack_500\n($20500)",
        "type": "data_rack",
        "power": 0,
        "demand": 40,
        "inputs": [
          "Usable_Power",
          "Chilled_Water",
          "Internal_Network"
        ],
        "outputs": [
          "Data_Storage"
        ],
        "surface": 1600
      },
      "style": {
        "borderRadius": 8,
        "padding": 8,
        "backgroundColor": "#D1FAE5",
        "border": "1px solid #CBD5E1"
      },
      "width": 177,
      "height": 111
    },
    {
      "id": "data_rack_500-8",
      "type": "custom",
      "position": {
        "x": 969.7482024972066,
        "y": -49.414646101263145
      },
      "data": {
        "label": "Data_Rack_500\n($20500)",
        "type": "data_rack",
        "power": 0,
        "demand": 40,
        "inputs": [
          "Usable_Power",
          "Chilled_Water",
          "Internal_Network"
        ],
        "outputs": [
          "Data_Storage"
        ],
        "surface": 1600
      },
      "style": {
        "borderRadius": 8,
        "padding": 8,
        "backgroundColor": "#D1FAE5",
        "border": "1px solid #CBD5E1"
      },
      "width": 177,
      "height": 111
    },
    {
      "id": "network_rack_100-9",
      "type": "custom",
      "position": {
        "x": 973.0659409415942,
        "y": 318.2429829990948
      },
      "data": {
        "label": "Network_Rack_100\n($8000)",
        "type": "network_rack",
        "power": 0,
        "demand": 75,
        "inputs": [
          "Usable_Power",
          "Chilled_Water"
        ],
        "outputs": [
          "Internal_Network",
          "Fresh_Water"
        ],
        "surface": 1600
      },
      "style": {
        "borderRadius": 8,
        "padding": 8,
        "backgroundColor": "#E5E7EB",
        "border": "1px solid #CBD5E1"
      },
      "width": 177,
      "height": 111
    },
    {
      "id": "transformer_5000-1",
      "type": "custom",
      "position": {
        "x": 97.95108123061917,
        "y": 91.47962745852331
      },
      "data": {
        "label": "Transformer_5000\n($250000)",
        "type": "transformer",
        "power": 5000,
        "demand": 0,
        "inputs": [
          "Grid_Connection"
        ],
        "outputs": [
          "Usable_Power"
        ],
        "surface": 40000
      },
      "style": {
        "borderRadius": 8,
        "padding": 8,
        "backgroundColor": "#D1FAE5",
        "border": "1px solid #CBD5E1"
      },
      "width": 177,
      "height": 111
    }
  ],
  "edges": [
    {
      "source": "water_supply_500-2",
      "sourceHandle": "Fresh_Water-out",
      "target": "water_treatment_250-3",
      "targetHandle": "Fresh_Water-in",
      "type": "custom",
      "data": {
        "label": "Fresh_Water"
      },
      "id": "reactflow__edge-water_supply_500-2Fresh_Water-out-water_treatment_250-3Fresh_Water-in"
    },
    {
      "source": "water_treatment_250-3",
      "sourceHandle": "Distilled_Water-out",
      "target": "water_chiller_400-4",
      "targetHandle": "Distilled_Water-in",
      "type": "custom",
      "data": {
        "label": "Distilled_Water"
      },
      "id": "reactflow__edge-water_treatment_250-3Distilled_Water-out-water_chiller_400-4Distilled_Water-in"
    },
    {
      "source": "water_chiller_400-4",
      "sourceHandle": "Chilled_Water-out",
      "target": "server_rack_500-5",
      "targetHandle": "Chilled_Water-in",
      "type": "custom",
      "data": {
        "label": "Chilled_Water"
      },
      "id": "reactflow__edge-water_chiller_400-4Chilled_Water-out-server_rack_500-5Chilled_Water-in"
    },
    {
      "source": "server_rack_500-5",
      "sourceHandle": "External_Network-out",
      "target": "server_square-6",
      "targetHandle": "External_Network-in",
      "type": "custom",
      "data": {
        "label": "External_Network"
      },
      "id": "reactflow__edge-server_rack_500-5External_Network-out-server_square-6External_Network-in"
    },
    {
      "source": "water_chiller_400-4",
      "sourceHandle": "Chilled_Water-out",
      "target": "data_rack_500-8",
      "targetHandle": "Chilled_Water-in",
      "type": "custom",
      "data": {
        "label": "Chilled_Water"
      },
      "id": "reactflow__edge-water_chiller_400-4Chilled_Water-out-data_rack_500-8Chilled_Water-in"
    },
    {
      "source": "water_chiller_400-4",
      "sourceHandle": "Chilled_Water-out",
      "target": "data_rack_500-7",
      "targetHandle": "Chilled_Water-in",
      "type": "custom",
      "data": {
        "label": "Chilled_Water"
      },
      "id": "reactflow__edge-water_chiller_400-4Chilled_Water-out-data_rack_500-7Chilled_Water-in"
    },
    {
      "source": "network_rack_100-9",
      "sourceHandle": "Internal_Network-out",
      "target": "data_rack_500-7",
      "targetHandle": "Internal_Network-in",
      "type": "custom",
      "data": {
        "label": "Internal_Network"
      },
      "id": "reactflow__edge-network_rack_100-9Internal_Network-out-data_rack_500-7Internal_Network-in"
    },
    {
      "source": "network_rack_100-9",
      "sourceHandle": "Internal_Network-out",
      "target": "data_rack_500-8",
      "targetHandle": "Internal_Network-in",
      "type": "custom",
      "data": {
        "label": "Internal_Network"
      },
      "id": "reactflow__edge-network_rack_100-9Internal_Network-out-data_rack_500-8Internal_Network-in"
    },
    {
      "source": "data_rack_500-8",
      "sourceHandle": "Data_Storage-out",
      "target": "server_square-6",
      "targetHandle": "Data_Storage-in",
      "type": "custom",
      "data": {
        "label": "Data_Storage"
      },
      "id": "reactflow__edge-data_rack_500-8Data_Storage-out-server_square-6Data_Storage-in"
    },
    {
      "source": "data_rack_500-7",
      "sourceHandle": "Data_Storage-out",
      "target": "server_square-6",
      "targetHandle": "Data_Storage-in",
      "type": "custom",
      "data": {
        "label": "Data_Storage"
      },
      "id": "reactflow__edge-data_rack_500-7Data_Storage-out-server_square-6Data_Storage-in"
    },
    {
      "source": "server_rack_500-5",
      "sourceHandle": "Processing-out",
      "target": "server_square-6",
      "targetHandle": "Processing-in",
      "type": "custom",
      "data": {
        "label": "Processing"
      },
      "id": "reactflow__edge-server_rack_500-5Processing-out-server_square-6Processing-in"
    },
    {
      "source": "server_square-6",
      "sourceHandle": "Water_Connection-out",
      "target": "water_supply_500-2",
      "targetHandle": "Water_Connection-in",
      "type": "custom",
      "data": {
        "label": "Water_Connection"
      },
      "id": "reactflow__edge-server_square-6Water_Connection-out-water_supply_500-2Water_Connection-in"
    },
    {
      "id": "edge-t1",
      "source": "transformer_5000-1",
      "sourceHandle": "Usable_Power-out",
      "target": "water_treatment_250-3",
      "targetHandle": "Usable_Power-in",
      "type": "custom",
      "data": {
        "label": "Usable_Power"
      }
    },
    {
      "id": "edge-t2",
      "source": "transformer_5000-1",
      "sourceHandle": "Usable_Power-out",
      "target": "water_chiller_400-4",
      "targetHandle": "Usable_Power-in",
      "type": "custom",
      "data": {
        "label": "Usable_Power"
      }
    },
    {
      "id": "edge-t3",
      "source": "transformer_5000-1",
      "sourceHandle": "Usable_Power-out",
      "target": "server_rack_500-5",
      "targetHandle": "Usable_Power-in",
      "type": "custom",
      "data": {
        "label": "Usable_Power"
      }
    },
    {
      "id": "edge-t4",
      "source": "transformer_5000-1",
      "sourceHandle": "Usable_Power-out",
      "target": "data_rack_500-8",
      "targetHandle": "Usable_Power-in",
      "type": "custom",
      "data": {
        "label": "Usable_Power"
      }
    },
    {
      "id": "edge-t5",
      "source": "transformer_5000-1",
      "sourceHandle": "Usable_Power-out",
      "target": "data_rack_500-7",
      "targetHandle": "Usable_Power-in",
      "type": "custom",
      "data": {
        "label": "Usable_Power"
      }
    },
    {
      "id": "edge-t6",
      "source": "server_square-6",
      "sourceHandle": "Grid_Connection-out",
      "target": "transformer_5000-1",
      "targetHandle": "Grid_Connection-in",
      "type": "custom",
      "data": {
        "label": "Grid_Connection"
      }
    }
  ]
}
"""

current="""
And the current configuration (budget, power, water, etc.) is:
[
  {
    "_id": {
      "$oid": "6816bc0234d36b78af59db3e"
    },
    "projectName": "HackUPC2025",
    "companyName": "LleidaHackers",
    "country": "Spain",
    "totalBudget": 2000000,
    "space_x": 500,
    "space_y": 300,
    "type": "server",
    "latituid": "41.387",
    "longitud": "2.168",
    "status": "Active",
    "budget": 960600,
    "powerConsume": 1985,
    "powerRequired": 0,
    "accomulatePower": -5000,
    "occupedSurface": 51900,
    "totalSurface": 150000,
    "waterUsage": 0,
    "distilledWaterUsage": 400,
    "chilledWaterUsage": 69,
    "waterProduction": 0,
    "freshWaterUsage": 250,
    "freshWaterProduction": 527,
    "distilledWaterProduction": 874,
    "chilledWaterProduction": 780,
    "internalNetworkUsage": 72,
    "internalNetworkProduction": 200,
    "externalNetworkProduction": 400,
    "soundLevel": 0,
    "procesProduction": 1000,
    "dataStorageProduction": 1000
  }
]

"""

objective="""
Your objective is to add a new module to the current configuration.
This module has to add power to the configuration.
"""



# Armar el prompt como texto plano
prompt = f"""
{context}
{total}
{current}
{objective}

You need to return a new module with the correct edges. 
Return only the new module and the edges that connect it to the current configuration in JSON format.
"""

def generate_response():
    response = client.models.generate_content(
        model="gemini-2.0-flash",
        contents=prompt,
    )
    return response