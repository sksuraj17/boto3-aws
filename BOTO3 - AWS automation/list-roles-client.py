import boto3

aws_management_console = boto3.Session(profile_name="default")
iam_console = aws_management_console.client("iam")

# --> To display the list of roles and count using client 

count = 0
for roles in iam_console.list_roles()["Roles"]:
    print(roles["RoleName"])
    count += 1
print(count)