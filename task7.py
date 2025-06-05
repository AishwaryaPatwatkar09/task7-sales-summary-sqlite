import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

# Connect to the database
conn = sqlite3.connect("sales_data.db")

# SQL Query
query = '''
    SELECT product, 
           SUM(quantity) AS total_qty, 
           SUM(quantity * price) AS revenue 
    FROM sales 
    GROUP BY product
'''

# Load data into pandas
df = pd.read_sql_query(query, conn)
print("Sales Summary:\n", df)

# Plotting
df.plot(kind='bar', x='product', y='revenue', title="Revenue by Product", legend=False)
plt.xlabel("Product")
plt.ylabel("Revenue")
plt.tight_layout()
plt.savefig("sales_chart.png")
plt.show()

# Close the connection
conn.close()
