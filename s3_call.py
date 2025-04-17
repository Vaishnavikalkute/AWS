import boto3


s3client=boto3.resource("s3")

# my_obj=s3client.get_object(Bucket="Name",key="obj_name")

# high level access
# list all the buckets in the aws s3
for bucket in s3client.buckets.all():
    print(bucket.name)

# list objects in buckets

bucket="myfirstbucket11-04-2025"
for obj in s3client.Bucket(bucket).objects.all():
    print(obj.key)

# upload the file in s3

s3client.Bucket(bucket).upload_file('test.txt','s3_file.txt')

print("#######################current obj")
for obj in s3client.Bucket(bucket).objects.all():
    print(obj.key)

# download file

# s3client.Bucket(bucket).download_file('s3_file.txt','local.txt')

# delete file
obj=s3client.Object(bucket,'s3_file.txt')
obj.delete()

print("current obj")
for obj in s3client.Bucket(bucket).objects.all():
    print(obj.key)