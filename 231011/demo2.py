import boto3, dynamodbinfo

#Scanning : Full Scan : api '

table=dynamodbinfo.dynamodb.Table('Movies')

results=table.scan() #Full Scan시 사용하는 api
# print(type(items)) #dict
# print(items.keys()) #'Items', 'Count', 'ScannedCount', 'ResponseMetadata'
# print(results['Count'], results['ScannedCount'])
items = results['Items']
for i in range(len(items)) :
    print(items[i]) # SELECT * FROM MOIVES
    
