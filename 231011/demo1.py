import boto3,dynamodbinfo
# client = boto3.client('dynamodb')
table = dynamodbinfo.dynamodb.Table('Movies')
item = {
    'Code':'19780080',
    'Name':'Star Wars',
    'Genre':'SF',
    'Date':'1978-04-12',
    'Director':'George Lucas', 
    'Actor':'마크 해밀, 캐리 피셔, 해리슨 포드, 알렉 기네'
}
table.put_item(Item=item)

item={
    'Code':'20050112',
    'Name':'Batman Begins',
    'Running Time' : 134,
    'Genre':'범죄, 액션, 판타지',
    'Date':'2005-06-24',
    'Director':'크리스토퍼',
    'Actor':'리암니슨, 크리스찬 베일 , 마이클 케인'
}
table.put_item(Item=item)

item = {'Code':'20180129', 'Name':'Get Out', 'Running Time' : 120, 'Genre':'호러', 'Date':'20128-01-29','Director':'마이클 조던', 'Actor':'마이클 벤슨'} 
table.put_item(Item=item)