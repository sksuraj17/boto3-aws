import boto3

aws_management_console = boto3.Session(profile_name="default")
iam_console = aws_management_console.resource("iam")

# --> To display the list of iam users

for user in iam_console.users.all():
     print(user.name)


# --> To display the list of roles and count

count = 0
for roles in iam_console.roles.all():
    count += 1
    print(roles)
print("Roles count: ", count)





