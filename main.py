import requests
import os
import csv
import sqlite3
from sqlite3 import OperationalError
import  pandas as pd
#need dotennv and load_dotenv for environment variable
#pip install python-dotenv
from dotenv import load_dotenv
load_dotenv()

#NOTE use sqlite sqlalchemy, sort csv as db instead. look at day 63 for how to do it

file = 'megaGymDataset.csv'
sqlfile = 'megaGymDataset.sql'
dbfile = 'gymdataset.db'





def pandy():
    # ,Title,Desc,Type,BodyPart,Equipment,Level,Rating,RatingDesc
    panda_data = pd.read_csv(file)
    print(panda_data["Title"]) #prints exercise column
    print(panda_data["Desc"]) #prints temp column
    print(panda_data["BodyPart"]) #prints temp column
    print(panda_data["Equipment"]) #prints temp column
    print(panda_data["Level"]) #prints temp column
    print(panda_data["Rating"]) #prints temp column
    print(panda_data["RatingDesc"]) #prints temp column


#APISs
#FoodData central, national nutrient database for standard reference https://fdc.nal.usda.gov/
#nutritionix worlds largest verified nutrition database https://developer.nutritionix.com/

