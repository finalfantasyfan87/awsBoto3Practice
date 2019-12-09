import boto3
s3 = boto3.client('s3')
""" :type : pyboto3.s3 """
file = input('File-including path-to be uploaded: ')
bucket_to_upload = input('Name of S3 bucket to upload file to: ')
s3Key = input('Filename that will be used as a S3 key: ' )

s3.upload_file(file,bucket_to_upload,s3Key)

print('If you received no errors, more than likely your file was successfully uploaded to your bucket. Please verify in your S3 AWS account')