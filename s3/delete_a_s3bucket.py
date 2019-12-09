import boto3
s3 = boto3.client('s3')
""" :type : pyboto3.s3 """
#prompt user for bucket name
bucket_to_delete = input("Please enter the exact name of the bucket you want to delete: ")
print(bucket_to_delete)
# verify bucket is gone...if it isn't you probaly got an error or it might being the process of deleting
s3.delete_bucket(Bucket=bucket_to_delete)
