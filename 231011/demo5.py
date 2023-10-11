import boto3, dynamodbinfo

# Delete
table = dynamodbinfo.dynamodb.Table('Movies')
table.delete_item(
    Key = {
        'Name' : 'Get Out', 'Code' : '20180129'
    }
)
