import duckdb

# Connect to DuckDB database
con = duckdb.connect(database='main.db')

# Tables to count rows
tables = ['bike_data', 'central_park_weather', 'fhv_tripdata', 'fhvhv_tripdata', 'green_tripdata', 'yellow_tripdata', 'fhv_bases']

# Print table name and row count
for table in tables:
    result = con.execute(f"SELECT COUNT(*) FROM {table}").fetchone()
    print(f"{table}: {result[0]}")

