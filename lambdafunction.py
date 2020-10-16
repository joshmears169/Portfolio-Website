import boto3
import json

#def lambda_handler(event, context):
   
dynamodb = boto3.resource('dynamodb')
   
table = dynamodb.Table('Visitors')
   
response = table.get_item(
    Key={
        'website': 'joshmearsportfolio'
     }
   )
count = response['Item']
print(count)

def update_count(): 
    count['visitors'] += 1
    return count

print(update_count())

table.put_item(Item=count)
