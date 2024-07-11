import duckdb
import os
import glob

# Connect to DuckDB (create a new database file or connect to an existing one)
conn = duckdb.connect('homework.db')

# Define the path to your downloaded data
local_path = '/usr/local/share/zsh/site-functions/data'

# List files in the directory to make sure they are there
print("Files in the directory:")
for root, dirs, files in os.walk(local_path):
    for file in files:
        print(os.path.join(root, file))

# Function to load CSV files
def load_csv(file_path):
    conn.execute(f"""
    CREATE TABLE IF NOT EXISTS {os.path.basename(file_path).split('.')[0]} AS
    SELECT * FROM read_csv_auto('{file_path}')
    """)

# Function to load Parquet files
def load_parquet(file_path):
    conn.execute(f"""
    CREATE TABLE IF NOT EXISTS {os.path.basename(file_path).split('.')[0]} AS
    SELECT * FROM read_parquet('{file_path}')
    """)

# Find and load all data files into DuckDB
csv_files = glob.glob(f'{local_path}/**/*.csv', recursive=True)
parquet_files = glob.glob(f'{local_path}/**/*.parquet', recursive=True)

for csv_file in csv_files:
    print(f"Importing {csv_file} into DuckDB")
    load_csv(csv_file)

for parquet_file in parquet_files:
    print(f"Importing {parquet_file} into DuckDB")
    load_parquet(parquet_file)

print("Data ingestion complete.")

