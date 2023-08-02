import boto3

aws_management_console = boto3.Session(profile_name="default")
iam_console = aws_management_console.client("iam")

userkey = 0

def users():
    users = []
    for user in iam_console.list_users()["Users"]:
        #  print(user["UserName"])
        users.append(user["UserName"])
    print(users)


def users_count():
    users_count = 0
    for user in iam_console.list_users()["Users"]:
        users_count += 1
    print(users_count)


def roles():
    roles = []
    for role in iam_console.list_roles()["Roles"]:
        # print(role["RoleName"])
        roles.append(role["RoleName"])
    print(roles)

def roles_count():
    roles_count = 0
    for role in iam_console.list_roles()["Roles"]:
        roles_count += 1
    print(roles_count)

def create_new_user(username):
    user = iam_console.create_user(
        UserName=username
    )
    print('--> User "new-user" created!')
    users()


def delete_new_user(username):

    user = iam_console.delete_user(
        UserName=username
    )
    print('--> User "new-user" deleted!')
    users()


options = """ \n<--- IAM HELP --->
1. List users
2. Display user count
3. List roles
4. Display role count
5. Create CLI user
6. Delete CLI user
7. Exit program
"""

while True:
    print(options)

    user_input = int(input("Enter your choice (1, 2, 3, 4, 5, 6) or 7 to exit: "))

    if(user_input == 1):
        users()
    elif(user_input == 2):
        users_count()
    elif(user_input == 3):
        roles()
    elif(user_input == 4):
        roles_count()
    elif(user_input == 5):
        print("Existing users")
        users()
        username = input("Enter the new user's username: ")
        create_new_user(username)
    elif(user_input == 6):
        print("Existing users")
        users()
        username = input("Enter the username to delete user: ")
        delete_new_user(username)
    elif(user_input == 7):
        print("Closing the program...")
        break
    else:
        print("Pl choose from the available options")