Task 7: Basic Sales Summary using SQLite & Python

📋 Description
This task is part of a Data Analyst Internship assignment. The objective is to create a small SQLite database of sales records and use Python to:
- Connect to the database
- Run SQL queries to calculate total quantity and revenue per product
- Display the results using `print()`
- Visualize revenue using a simple matplotlib bar chart

🛠 Tools Used
- Python
- SQLite (`sqlite3`)
- Pandas
- Matplotlib

📁 Files Included
- `create_db.py` → Creates and populates `sales_data.db` with sample sales data
- `sales_data.db` → SQLite database with a single `sales` table
- `task7.py` → Main script to query, print and plot sales summary
- `sales_chart.png` → Bar chart showing revenue per product
- `README.md` → This file

🔍 Sample Output
- Total quantity and revenue per product shown in terminal
- Bar chart saved as `sales_chart.png`

🧠 Key Concepts Learned
- Using SQL inside Python
- Aggregating data with SQL (`SUM`, `GROUP BY`)
- Reading SQL results into a pandas DataFrame
- Basic data visualization with matplotlib

✅ How to Run
```bash
# Step 1: Create and populate the database
python create_db.py

# Step 2: Run the analysis and see the chart
python task7.py
