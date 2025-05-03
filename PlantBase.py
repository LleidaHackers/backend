class PlantBase:
    def __init__(self, plant_name, company, country, budget, space_x, space_y, lat, long):
        self.name = plant_name
        self.company = company
        self.country = country
        self.budget = budget
        self.space_x = space_x
        self.space_y = space_y
        self.lat = lat
        self.long = long


    def __str__(self):
        return f"Plant Name: {self.plant_name}, Type: {self.plant_type}, Sunlight Needs: {self.sunlight_needs}, Water Needs: {self.water_needs}"