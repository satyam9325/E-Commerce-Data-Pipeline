import json
from datetime import *
import boto3
from mock_data_generator import genearate_data
from upload_to_s3 import upload_to_s3

start_date = date(2025,4,25)
end_date = date.today()



def lambda_handler(event,context):
    for i in range((end_date-start_date).days+1):
        current_date = start_date + timedelta(days=i)
        genearate_data(current_date)
        upload_to_s3(f"transactions_{str(current_date)}.csv",current_date )

    return {
        'statusCode': 200,
        'body': json.dumps(f'Ecommerce Data Generated!!!')
    }