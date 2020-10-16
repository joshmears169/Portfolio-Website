import boto3


def create_visitor_table(dynamodb=None):
    if not dynamodb:
        dynamodb = boto3.resource('dynamodb', region_name='eu-west-2')

    table = dynamodb.create_table(
        TableName='Visitors',
        KeySchema=[
            {
                'AttributeName': 'website',
                'KeyType': 'HASH'  # Partition key
            },
        ],
        AttributeDefinitions=[
            {
                'AttributeName': 'website',
                'AttributeType': 'S'
            },
        ],
        ProvisionedThroughput={
            'ReadCapacityUnits': 10,
            'WriteCapacityUnits': 10
        }
    )
    return table


if __name__ == '__main__':
    visitor_table = create_visitor_table()
    print("Table status:", visitor_table.table_status)