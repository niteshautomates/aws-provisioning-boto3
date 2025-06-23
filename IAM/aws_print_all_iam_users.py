import boto3
import boto3.session


aws_management_console = boto3.session.Session(profile_name="default")

iam_console_resources = aws_management_console.resource("iam")
iam_console_client = aws_management_console.client("iam")

for each_user in iam_console_resources.users.all():
    print(f"User: {each_user.name}")



for each_user in iam_console_client.list_users()['Users']:
    print(f"User Using Client: {each_user['UserName']}")
