import glob, os
import boto3

# set up S3 client
s3 = boto3.client('s3')

# upload file to S3 bucket
bucket_name = 'traffic-low'

#path must be change to your local path
os.chdir("//home/pc-work/Downloads/gd")
for file in glob.glob("*.zip"):
    s3.upload_file(file, bucket_name, file)
    print(f"{file} -file uploaded")