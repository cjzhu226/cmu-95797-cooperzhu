-- Ingest bike_data. Create the table
CREATE TABLE bike_data AS SELECT * FROM read_csv_auto('/Users/cooperzhu/cmu-95797-cooperzhu/data/citibike-tripdata.csv.gz');

-- Ingest central_park_weather. Create the table
CREATE TABLE central_park_weather AS SELECT * FROM read_csv_auto('/Users/cooperzhu/cmu-95797-cooperzhu/data/central_park_weather.csv');

-- Ingest fhv_tripdata. Create the table
CREATE TABLE fhv_tripdata AS SELECT * FROM read_parquet('/Users/cooperzhu/cmu-95797-cooperzhu/data/taxi/fhv_tripdata.parquet');

-- Ingest fhvhv_tripdata. Create the table
CREATE TABLE fhvhv_tripdata AS SELECT * FROM read_parquet('/Users/cooperzhu/cmu-95797-cooperzhu/data/taxi/fhvhv_tripdata.parquet');

-- Ingest green_tripdata. Create the table
CREATE TABLE green_tripdata AS SELECT * FROM read_parquet('/Users/cooperzhu/cmu-95797-cooperzhu/data/taxi/green_tripdata.parquet');

-- Ingest yellow_tripdata. Create the table
CREATE TABLE yellow_tripdata AS SELECT * FROM read_parquet('/Users/cooperzhu/cmu-95797-cooperzhu/data/taxi/yellow_tripdata.parquet');

-- Ingest fhv_bases. Create the table
CREATE TABLE fhv_bases AS SELECT * FROM read_csv_auto('/Users/cooperzhu/cmu-95797-cooperzhu/data/fhv_bases.csv');

