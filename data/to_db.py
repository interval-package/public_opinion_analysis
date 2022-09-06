import sqlite3
import pandas as pd

sql = sqlite3.connect("database.db")

pd.read_csv("data.csv").to_sql(name="hot",con=sql)

