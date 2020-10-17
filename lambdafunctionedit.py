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

def update_count(): 
    count['visitors'] += 1
    return count

update_count()

table.put_item(Item=count)

response = table.get_item(
    Key={
        'website': 'joshmearsportfolio'
    }
)

count = response['Item']

print(count)