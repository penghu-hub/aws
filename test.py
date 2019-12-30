import boto3

# Let's use Amazon S3
s3 = boto3.resource('s3')

for bucket in s3.buckets.all():
    print(bucket.name)

ec2 = boto3.resource('ec2')

for instance in ec2.instances.all():
    print(instance.name)

client = boto3.client('iam')

response = client.list_groups(
)

print(response)
