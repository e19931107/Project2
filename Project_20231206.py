from pathlib import Path
import pandas as pd
import mysql.connector
from mysql.connector import Error

project = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Ff301128"
    )

mycursor = project.cursor()

current_path = Path()/'CSV'
for folder in current_path.absolute().glob('*'):
    print(folder)

