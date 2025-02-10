import boto3
def create_EC2_instance():
    try:
        print("Creating EC2 Instance")
        resource_ec2=boto3.client("ec2",region_name="eu-north-1")
        resource_ec2.run_instances(
            ImageId = "ami-08b1d20c6a69a7100",
            MinCount = 1,
            MaxCount = 1,
            InstanceType = "t3.micro",
            KeyName = "xyza"
            )
    except Exception as E:
        print(E)

create_EC2_instance()