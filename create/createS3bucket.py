""" :type : pyboto3.s3 """
import boto3
s3 = boto3.client('s3')

s3.create_bucket(Bucket='jens-bucket')