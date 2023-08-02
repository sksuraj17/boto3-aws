import boto3
from pprint import pprint
aws_management_console = boto3.Session(profile_name="default")
ec2_console = aws_management_console.client(service_name="ec2")

request = ec2_console.describe_instances()["Reservations"]
for value in request:
    for instance in value["Instances"]:
        pprint(instance["InstanceId"])
