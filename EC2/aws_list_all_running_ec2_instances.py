import boto3


class ListEC2Instance:
    def __init__(self, ec2_client):
        self.ec2_client = ec2_client

    def list_running_instances(self):
        try:
            response = self.ec2_client.describe_instances(
                Filters=[{'Name': 'instance-state-name', 'Values': ['running']}]
            )
            instances = []
            for reservation in response['Reservations']:
                for instance in reservation['Instances']:
                    instances.append({
                        'InstanceId': instance['InstanceId'],
                        'InstanceType': instance['InstanceType'],
                        'PublicIpAddress': instance.get('PublicIpAddress'),
                        'PrivateIpAddress': instance.get('PrivateIpAddress'),
                        'State': instance['State']['Name']
                    })
            return instances
        except Exception as e:
            print(f"Error listing running instances: {e}")
            return []

ec2_client= boto3.client("ec2")
obj =    ListEC2Instance(ec2_client)
lists=obj.list_running_instances()

for instance in lists:
    print(f"Instance ID: {instance['InstanceId']}")