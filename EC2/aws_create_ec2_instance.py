import boto3

class EC2InstanceCreator:
    def __init__(self, name, region, instance_type, key_name, security_groups_ids, image_id):
        self.name = name
        self.region = region
        self.instance_type = instance_type
        self.key_name = key_name
        self.security_groups_ids = security_groups_ids
        self.image_id = image_id

    def create_instance(self):
        response = boto3.client("ec2", region_name=self.region).run_instances(
            ImageId=self.image_id,
            InstanceType=self.instance_type,
            KeyName=self.key_name,
            SecurityGroupIds=self.security_groups_ids,
            MinCount=1,
            MaxCount=1,
            TagSpecifications=[
                {
                    'ResourceType': 'instance',
                    'Tags': [
                        {
                            'Key': 'Name',
                            'Value': self.name
                        }
                    ]
                }
            ]
        )

obj =  EC2InstanceCreator("server_boto3_demo" , "ap-south-1", "t2.micro", "ssh_key_ap", ["sg-0c96e79e1d37f5551"], "ami-0f918f7e67a3323f0")
print("Creating instance...")
obj.create_instance()