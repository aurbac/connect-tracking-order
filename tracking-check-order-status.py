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
            KeyConditionExpression='order_id = :order_id',
            ExpressionAttributeValues={ ":order_id" : { "S" : event['Details']['ContactData']['Attributes']['secretnumber'] } }
        )
    except ClientError as e:
        print(e.response['Error']['Message'])
        resultMap = {"message": "Los siento, número de orden no encontrada.", "result":True}
    else:
        #item = response['Item']
        print(json.dumps(response))
        if len(response['Items'])>0:
            resultMap = {"message": "Tu paquete tiene el siguiente estado: " + response['Items'][0]['status']['S'] + ". Gracias.","result":True}
        else:
            resultMap = {"message": "Los siento, número de orden no encontrada.", "result":True}
    return resultMap
