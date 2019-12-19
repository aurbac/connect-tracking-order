import json
import boto3
from botocore.exceptions import ClientError
import os

def lambda_handler(event, context):
    print(json.dumps(event))
    TABLE_NAME = os.environ['TABLE_NAME']
    dynamodb = boto3.client('dynamodb')
    try:
        response = dynamodb.query(
            TableName=TABLE_NAME,
            KeyConditionExpression='phone_number = :phone_number',
            ExpressionAttributeValues={ ":phone_number" : { "S" : event['Details']['ContactData']['CustomerEndpoint']['Address'] } }
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
        resultMap = {"result":False}
    else:
        #item = response['Item']
        print(json.dumps(response))
        if len(response['Items'])>0:
            resultMap = {"phone_number":response['Items'][0]['phone_number']['S'],"first_name":response['Items'][0]['first_name']['S'],"result":True}
        else:
            resultMap = {"result":False}
    return resultMap
