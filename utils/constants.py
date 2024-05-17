import configparser
import os

parser = configparser.ConfigParser()
parser.read(os.path.join(os.path.dirname(__file__),'../config/config.conf'))

REDDIT_CLIENT_ID = parser.get('api_keys','reddit_client_id')
REDDIT_CLIENT_SECRET = parser.get('api_keys','reddit_secret_key')

INPUT_PATH = parser.get('file_paths','input_path')
OUTPUT_PATH = parser.get('file_paths','output_path')

AWS_ACCESS_KEY_ID = parser.get('aws_keys','aws_access_key_id')
AWS_SECRET_KEY = parser.get('aws_keys','aws_secret_access_key')
AWS_REGION = parser.get('aws_keys','aws_region')
AWS_BUCKET_NAME = parser.get('aws_keys','aws_bucket_name')