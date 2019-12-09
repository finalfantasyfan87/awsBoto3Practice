import os

import boto3
s3 = boto3.client('s3')
""" :type : pyboto3.s3 """
my_buckies = s3.list_buckets()
for bucket in my_buckies['Buckets']:
    print('Bucket', bucket)
    
#Prints the follow:
# Bucket {'Name': 'aws-codestar-us-west-2-199186439076-cityofchicagoda-pipe', 'CreationDate': datetime.datetime(2019, 12, 9, 1, 35, 20, tzinfo=tzutc())}
# Bucket {'Name': 'elasticbeanstalk-us-east-2-199186439076', 'CreationDate': datetime.datetime(2018, 6, 5, 18, 13, 35, tzinfo=tzutc())}
# Bucket {'Name': 'elasticbeanstalk-us-west-1-199186439076', 'CreationDate': datetime.datetime(2019, 12, 9, 1, 34, 20, tzinfo=tzutc())}
# Bucket {'Name': 'elasticbeanstalk-us-west-2-199186439076', 'CreationDate': datetime.datetime(2019, 5, 28, 3, 36, 21, tzinfo=tzutc())}
# Bucket {'Name': 'jens-buckie', 'CreationDate': datetime.datetime(2019, 12, 9, 5, 1, 38, tzinfo=tzutc())}
# Process finished with exit code 0