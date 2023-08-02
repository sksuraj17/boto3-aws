import boto3

aws_management_console = boto3.Session(profile_name="default")
ec2_console = aws_management_console.client(service_name="ec2")

def run_t2_nano(instance_count):
    ec2_console.run_instances(
        ImageId = "ami-0f34c5ae932e6f0e4",
        InstanceType = "t2.nano",
        MaxCount = instance_count,
        MinCount = 1,
        SubnetId = 'subnet-0f9f6e5def7a50ef5'
    )

def run_t2_micro(instance_count):
    ec2_console.run_instances(
        ImageId = "ami-0f34c5ae932e6f0e4",
        InstanceType = "t2.micro",
        MaxCount = instance_count,
        MinCount = 1,
        SubnetId = 'subnet-0f9f6e5def7a50ef5'
    )

options = """ \n<--- SELECT THE INSTANCE TYPE --->
1. t2.nano
2. t2.micro
"""

print(options)

user_input = int(input("Enter your choice to continue: "))

if(user_input == 1):
    instance_count = int(input("Enter the number of instances to start: "))
    run_t2_nano(instance_count)
    print("Instance created")
elif(user_input == 2):
    instance_count = int(input("Enter the number of instances to start: "))
    run_t2_micro(instance_count)
    print("Instance created")

else:
    print("Pl choose from the available options")