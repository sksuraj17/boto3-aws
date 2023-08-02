import boto3

aws_management_console = boto3.Session(profile_name="default")
iam_console_resource = aws_management_console.resource("iam")
iam_console_client = aws_management_console.client("iam")

# --> To display the list of iam users using resource 

for user in iam_console_resource.users.all():
     print(user.name)

# --> To display the list of iam users using client 

for user in iam_console_client.list_users()["Users"]:
     print(user["UserName"])
