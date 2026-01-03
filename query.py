import sqlite3
import pandas as pd

# Connect to database
conn = sqlite3.connect("database.db")

# Write SQL query
query = """
SELECT title, price
FROM books
WHERE price > 30
ORDER BY price DESC;
"""

# Execute query and load into DataFrame
df = pd.read_sql_query(query, conn)
df.to_csv("query_results.csv", index=False)
# Close connection
conn.close()

# Display results
print(df)
