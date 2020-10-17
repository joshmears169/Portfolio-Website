import boto3
import json
   
dynamodb = boto3.resource('dynamodb')
   
table = dynamodb.Table('Visitors')

response = table.get_item(
    Key={
        'website': 'joshmearsportfolio'
    }
)

count = response['Item']

count['visitors'] += 1

table.put_item(Item=count)

response = table.get_item(
    Key={
        'website': 'joshmearsportfolio'
    }
)

count = response['Item']

print(count)