import boto3
import json
   
dynamodb = boto3.resource('dynamodb')
   
table = dynamodb.Table('Visitors')

def lambda_handler(event, context):  

    response = table.get_item(
        Key={
            'website': 'joshmearsportfolio'
        }
    )
    count = response['Item']

    def update_count(): 
        count['visitors'] += 1
        return count

    table.put_item(Item=count)

    response = table.get_item(
        Key={
            'website': 'joshmearsportfolio'
        }
    )
    count = response['Item']

    return {
           'body': count
        }