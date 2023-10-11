import boto3, dynamodbinfo

# Update
table = dynamodbinfo.dynamodb.Table('Movies')
result= table.update_item(
    Key={
        'Code' : '20050112', 'Name' : 'Batman Begins'
    },
    UpdateExpression='SET Director = :val',
    ExpressionAttributeValues= { ':val' : '맷 리브스' }
)
#    변수의 값 :val 이고 이 :val 이 변경된 값을 나타내도록 형식을 셋팅한다
print(result['Item'])