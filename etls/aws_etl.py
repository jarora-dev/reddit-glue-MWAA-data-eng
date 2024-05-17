import s3fs
from utils.constants import AWS_ACCESS_KEY_ID, AWS_SECRET_KEY, AWS_REGION

def connect_to_s3():
    try:
        s3 = s3fs.S3FileSystem(anon=False, key=AWS_ACCESS_KEY_ID, secret=AWS_SECRET_KEY)
        return s3
    except Exception as e:
        print(f"Error connecting to S3: {e}")
    

def create_bucket_if_not_exist(s3, bucket_name):
    try:
        if not s3.exists(bucket_name):
            s3.mkdir(bucket_name)
            print(f"Bucket {bucket_name} created")
        else:
            print(f"Bucket {bucket_name} already exists")
    except Exception as e:
        print(f"Error creating bucket: {e}")


def upload_file_to_s3(s3, file_path, bucket_name, file_name):
    try:
        s3.put(file_path, f"{bucket_name}/raw/{file_name}")
        print(f"File {file_name} uploaded to {bucket_name}")
    except Exception as e:
        print(f"Error uploading file to S3: {e}")
        
