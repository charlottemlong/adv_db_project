import boto3

def delete_items_table(dynamodb=None):
    dynamodb = boto3.resource('dynamodb', endpoint_url="http://localhost:8000")

    # get items table so it can be deleted
    items_table = dynamodb.Table('Items')
    items_table.delete()


if __name__ == '__main__':
    delete_items_table()
    # Once successful,
    print("Table deleted.")