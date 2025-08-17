import requests
import os
import csv
import  pandas as pd
#need dotennv and load_dotenv for environment variable
#pip install python-dotenv
from dotenv import load_dotenv
load_dotenv()

#NOTE use sqlite sqlalchemy, sort csv as db instead. look at day 63 for how to do it

file = 'megaGymDataset.csv'

with open(file) as data_file:
        data = csv.reader(data_file)
        temperatures = [] #integers not string
        for row in data:
            print(row)

panda_data = pd.read_csv(file)
print(panda_data["Title"]) #prints temp column

#APISs
#FoodData central, national nutrient database for standard reference https://fdc.nal.usda.gov/
#nutritionix worlds largest verified nutrition database https://developer.nutritionix.com/

