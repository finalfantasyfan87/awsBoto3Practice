import os

import boto3
s3 = boto3.client('s3')
""" :type : pyboto3.s3 """
my_buckies = s3.list_buckets()
for bucket in my_buckies['Buckets']:
    print('Bucket', bucket)
