import boto3

def list_all_buckets_from_all_regions():
    response = boto3.client("s3")
    
    for bucket in response.list_buckets()["Buckets"]:
        bucket_name = bucket["Name"]
        
        location = response.get_bucket_location(Bucket=bucket_name)["LocationConstraint"]
        print(f"Bucket Name: {bucket_name} and Location: {location}")
        
        
def delete_all_s3_buckets():
    response = boto3.client("s3")        
    print("Deleting all S3 buckets")
    print("========================================")
    for bucket in response.list_buckets()["Buckets"]:
        bucket_name = bucket["Name"]
        print(f"Bucket Name: {bucket_name}")
        response.delete_bucket(Bucket=bucket_name)
        print(f"Bucket {bucket_name} deleted.")
        
        
list_all_buckets_from_all_regions()     
delete_all_s3_buckets()   