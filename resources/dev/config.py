import os

key = "youtube_project"
iv = "youtube_encyptyo"
salt = "youtube_AesEncryption"

#AWS Access And Secret key
aws_access_key = "pODrW9CTJTH9prbsT2PBBFNI+E9u9k6tYMijY46MF9c="
aws_secret_key = "GYD75b/03uzlnCcX7upSK6uvF94Y3iMYTOaIbzpUbU+u3ItZSAT9XHCvct1FJPC/"
bucket_name = "retail-sparkproject"
s3_customer_datamart_directory = "customer_data_mart"
s3_sales_datamart_directory = "sales_data_mart"
s3_source_directory = "sales_data/"
s3_error_directory = "sales_data_error/"
s3_processed_directory = "sales_data_processed/"


#Database credential
# MySQL database connection properties
DB_CONFIG = {
    "host": "localhost",
    "port": 3306,
    "user":"root",
    "password":"Shanty@1234",
    "database":"prasad",
}

url = f"jdbc:mysql://{DB_CONFIG['host']}:{DB_CONFIG['port']}/{DB_CONFIG['database']}"
properties = {
    "user": DB_CONFIG["user"],
    "password": DB_CONFIG["password"],
    "driver": "com.mysql.cj.jdbc.Driver"
}

# Table name
customer_table_name = "customer"
product_staging_table = "product_staging_table"
product_table = "product"
sales_team_table = "sales_team"
store_table = "store"

#Data Mart details
customer_data_mart_table = "customers_data_mart"
sales_team_data_mart_table = "sales_team_data_mart"

# Required columns
mandatory_columns = ["customer_id","store_id","product_name","sales_date","sales_person_id","price","quantity","total_cost"]


# File Download location
local_directory = "C:\\Users\\mahakal.s\\Documents\\Retail_Project\\file_from_s3\\"
customer_data_mart_local_file = "C:\\Users\\mahakal.s\\Documents\\Retail_Project\\customer_data_mart\\"
sales_team_data_mart_local_file = "C:\\Users\\mahakal.s\\Documents\\Retail_Project\\sales_team_data_mart\\"
sales_team_data_mart_partitioned_local_file = "C:\\Users\\mahakal.s\\Documents\\Retail_Project\\sales_partition_data\\"
error_folder_path_local = "C:\\Users\\mahakal.s\\Documents\\Retail_Project\\error_files\\"
