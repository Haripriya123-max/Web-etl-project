import sqlite3
import pandas as pd

conn = sqlite3.connect("database.db")
df = pd.read_csv("clean_data.csv")

df.to_sql("books", conn, if_exists="replace", index=False)

conn.close()
print("Data loaded into database")
