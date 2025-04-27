import boto3
from datetime import *
s3_client = boto3.client("s3")
bucket_name = "ecommerce-transaction-data"
current_date = date.today()

def upload_to_s3(filename, current_date):
    year = current_date.year
    month = current_date.month 
    date = current_date.date  
    filepath= f"transactions/year={year}/month={month}/date={date}/{filename}"
    s3_client.upload(f'/tmp/{filename}',filepath )
    print(f"File uploaded to S3 Bucket {bucket_name}/{filepath}")
    