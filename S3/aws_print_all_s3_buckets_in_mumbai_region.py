import boto3

def create_s3_bucket_in_mumbai_region(bucket_name):
    response = boto3.client("s3")
    
    for bucket in response.list_buckets()["Buckets"]:
        if bucket["Name"] == bucket_name:
            print(f"Bucket {bucket_name} already exists.")
            return
    else:  
        response.create_bucket(
        Bucket=bucket_name,
        CreateBucketConfiguration={
            "LocationConstraint": "ap-south-1"
        }
    )




def print_all_s3_buckets_in_mumbai_region(target_location):
    response = boto3.client("s3")
    print("Listing all S3 buckets in Mumbai region")
    print("========================================")
    print(response.list_buckets()["Buckets"])
    for bucket in response.list_buckets()["Buckets"]:
        bucket_name = bucket["Name"]
        location=response.get_bucket_location(Bucket=bucket_name)['LocationConstraint']
        if location == target_location:
            print(f"Bucket Name: {bucket_name} and Location: {location}")
        

def delete_s3_buckets_in_mumbai_region(bucket_name, target_location):
    response = boto3.client("s3")
    print("Deleting S3 buckets from Mumbai Region")
    print("========================================")
    for bucket in response.list_buckets()["Buckets"]:
        bucket_name = bucket["Name"]
        location = response.get_bucket_location(Bucket=bucket_name)['LocationConstraint']
        if location == target_location:
            print(f"Bucket Name: {bucket_name} and Location: {location}")
            response.delete_bucket(Bucket=bucket_name)
            print(f"Bucket {bucket_name} deleted.")






bucket_name = "my-test-bucket-in-mumbai-region-1234567890"
region_name = "ap-south-1"
create_s3_bucket_in_mumbai_region(bucket_name)
print_all_s3_buckets_in_mumbai_region(region_name)  # Mumbai region code is "ap-south-1"     
delete_s3_buckets_in_mumbai_region(bucket_name, region_name)  # Mumbai region code is "ap-south-1"