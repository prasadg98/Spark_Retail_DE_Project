import os

from resources.dev import config
from resources.dev.config import aws_access_key
from src.main.read.aws_read import S3Reader
from src.main.utility.encrypt_decrypt import *
from src.main.utility.my_sql_session import get_mysql_connection
from src.main.utility.s3_client_object import *
from src.main.utility.logging_config import *
from src.test.sales_data_upload_s3 import s3_client_provider
from src.test.scratch_pad import s3_client_provider, s3_absolute_file_path
from resources.dev.config import *
from src.main.read.aws_read import *

aws_access_key = config.aws_access_key

aws_secret_key = config.aws_secret_key

s3_client_provider = S3ClientProvider(decrypt(aws_access_key), decrypt(aws_secret_key))
s3_client = s3_client_provider.get_client()

#Now you can use s3_client for your s3 operations
response = s3_client.list_buckets()
print(response)
logger.info("List of Buckets: %s", response['Buckets'])

# Check if local directory already has a file
#If the file exists, then check if the same file is present in the staging area
#with status as A, IF so then do not delete and try re-running it
#Else give an error and do not process the next file
csv_files = [file for file in os.listdir(config.local_directory) if file.endswith(".csv")]
connection =get_mysql_connection()
cursor = connection.cursor()

total_csv_files =[]
if csv_files:
    for file in csv_files:
        total_csv_files.append(file)
    statement = f"select distinct file_name from " \
                f"{config.DB_CONFIG['database']}.{config.product_staging_table} "\
                f"where file_name in ({str(total_csv_files)[1:-1]}) and status = 'I'"

    logger.info(f"statement created dynamically: {statement} ")
    cursor.execute(statement)
    data = cursor.fetchall()
    if data:
        logger.info("Your last run was failed, please check")
    else:
        logger.info("No record match")

else:
    logger.info("Your last run was successful")

try:
    s3_reader = S3Reader()
    #Bucket name should come from the table
    folder_path = config.s3_source_directory
    s3_absolute_file_path = s3_reader.list_files(s3_client, config.bucket_name, folder_path=folder_path)
    logger.info("Absolute path on s3 bucket for csv file %s ",s3_absolute_file_path)
    if not s3_absolute_file_path:
       logger.info("No files available at {folder_path}")
       raise Exception("No Data available to process ")

except Exception as e:
    logger.error("Exited with error:- %s", e)
    raise e



