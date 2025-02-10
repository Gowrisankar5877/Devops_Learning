import boto3
def create_ec2_instances(instances, region):
    try:
        print("Creating EC2 Instances")
        ec2_client = boto3.client("ec2", region_name=region)
        for instance in instances:
            response = ec2_client.run_instances(
                ImageId=instance['image_id'],
                InstanceType=instance['instance_type'],
                KeyName=instance['key_name'],
                MinCount=instance.get('min_count', 1),
                MaxCount=instance.get('max_count', 1),
                TagSpecifications=[
                    {
                        'ResourceType': 'instance',
                        'Tags': [{'Key': 'Name', 'Value': instance['tag_name']}]
                    }
                ]
            )
            print(f"EC2 Instance '{instance['tag_name']}' Created Successfully!", response)
    except Exception as e:
        print("Error creating EC2 instances:", e)
instances_to_create = [
    {"image_id": "ami-08b1d20c6a69a7100", "instance_type": "t3.micro", "key_name": "xyza", "tag_name": "Instance1"},
    {"image_id": "ami-08b1d20c6a69a7100", "instance_type": "t3.micro", "key_name": "xyza", "tag_name": "Instance2"}
]
create_ec2_instances(instances_to_create, "eu-north-1")
