# Index Scanning 
import boto3, dynamodbinfo

table = dynamodbinfo.dynamodb.Table('Movies')

# print(table)
# index scanning = get_item()
# Using get_item
def main():
    result = table.get_item(
        Key={
            'Code' : '20050112',
            'Name' : 'Batman Begins'
        }
    )
    # print(type(result)) #dict
    # print(result.keys()) #dict_keys(['Item', 'ResponseMetadata'])
    print(result)

if __name__ =="__main__":
        main() 



