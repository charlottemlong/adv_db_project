from botocore.exceptions import ClientError
import boto3 
from boto3.dynamodb.conditions import Key

# Referenced: https://www.section.io/engineering-education/python-boto3-and-amazon-dynamodb-programming-tutorial/

def put_item(item_name, item_id, color, length, fabric, dynamodb=None):

    # Example call: put_item("Elliatt Espousal Sweetheart Mini Dress", 7, "Ivory", "33", "Polyester")
    # Example print: pprint(item_resp) (need to import pprint from pprint)

    dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")
    # Specify the table
    items_table = dynamodb.Table('Items')
    response = items_table.put_item(
        # Data to be inserted
        Item={
            'item_name': item_name,
            'item_id': item_id,
            'info': {
                'Color': color,
                'Length': length,
                'Fabric': fabric
            }
        }
    )
    return response

def delete_item(item_name, item_id, dynamodb=None):

    # Example Usage: delete_response = delete_item("Reformation Zenni Dress", 3)
    # Example Print: if delete_response: pprint(delete_response)

    dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")
    # Get items table
    items_table = dynamodb.Table('Items')

    try:
        response = items_table.delete_item(
            Key={
                'item_name': item_name,
                'item_id': item_id
            }
        )
    except ClientError as er:
        if er.response['Error']['Code'] == "FailedException":
            print(er.response['Error']['Message'])
        else:
            raise
    else:
        return response

def query_items(item_name, dynamodb=None):
    
    # Example query_id: query_id = "Selkie Strapless Mini Dress"
    # Example usage: items_data = query_items(query_id)
    # Example print: print(item_data['item_name'], ":", item_data['item_id']) for item_data in items_data

    dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")
    # Specify the table to query
    items_table = dynamodb.Table('Items')
    response = items_table.query(
        KeyConditionExpression=Key('item_name').eq(item_name)
    )
    return response['Items']

def get_item(item_name, item_id, dynamodb=None):

    # Example usage: item = get_item("Reformation Zenni Dress", 3,)
    # Example print: if item: print(item) 
    
    dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")
    # Get items table to read from
    items_table = dynamodb.Table('Items')

    try:
        response = items_table.get_item(
            Key={'item_name': item_name, 'item_id': item_id})
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return response['Item']
    
# A method for printing items
def print_items(items):
    for item in items:
        print(f"\n{item['item_name']} : {item['item_id']}")
        print(item['info'])

def scan_items(display_items_data, dynamodb=None):

    # Example usage: scan_items(print_items)

    dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")
    # Get items table
    items_table = dynamodb.Table('Items')
    done = False
    start_key = None
    while not done:
        # if start_key:
        #     scan_kwargs['ExclusiveStartKey'] = start_key
        response = items_table.scan()
        display_items_data(response.get('Items', []))
        start_key = response.get('LastEvaluatedKey', None)
        done = start_key is None

def update_item(item_name, item_id, color, leng, fabric, dynamodb=None):
    
    # Example usage: update_response = update_item("Reformation Zenni Dress", 3, "Ivory", "35", "Polyester")
    # Example print: pprint(update_response) (must import pprint from pprint)

    dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")
    # Specify the table
    items_table = dynamodb.Table('Items')

    response = items_table.update_item(
        Key={
            'item_name': item_name,
            'item_id': item_id
        },
        UpdateExpression="set info.Color=:color, info.#l=:leng, info.Fabric=:fabric",
        ExpressionAttributeValues={
            ':color': color,
            ':leng': leng,
            ':fabric': fabric,
        },
        ExpressionAttributeNames={
            "#l": "Length"
        },
        ReturnValues="UPDATED_NEW"
    )
    return response

if __name__ == '__main__':
    item = get_item("Farm Rio Banana Cover-Up Dress", 2)
    if item:
        # Print the data read
        print(item)