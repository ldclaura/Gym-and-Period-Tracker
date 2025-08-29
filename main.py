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

file = 'instance/megaGymDataset.csv'
sqlfile = 'instance/megaGymDataset.sql'
dbfile = 'instance/gymdataset.db'


def search_dataset(column, search):
    con = sqlite3.connect(dbfile)

    cur = con.cursor()
    
    if column.capitalize() == "Id":
        for row in cur.execute(f'SELECT * FROM gymdataset WHERE {column.capitalize()} LIKE "{search}";'):
            # print(row)
            con.close()
            return row
    else:
        all = []
        for row in cur.execute(f'SELECT * FROM gymdataset WHERE {column.capitalize()} LIKE "%{search}%";'):
            all.append(row)
        con.close()
        return tuple(all)

print(search_dataset("Id", "10"))



#APISs
#FoodData central, national nutrient database for standard reference https://fdc.nal.usda.gov/
#nutritionix worlds largest verified nutrition database https://developer.nutritionix.com/

