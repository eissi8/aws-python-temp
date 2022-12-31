import boto3
import random

rand_key=str(random.randint(0, 100000000))

ddb=boto3.client('dynamodb')

ddb.put_item(TableName='test', Item={"name": {"S":rand_key},"age":{"S":rand_key}})

#print(ddb.get_item(TableName='test',Key={"name": {"S":"junghun"},"age":{"S":"50"}}))
while True:
    ddb.get_item(TableName='test', Key={"name": {"S":rand_key},"age":{"S":rand_key}})

#while True:
#  ddb.get_item(TableName='test',Key={"name": {"S":"junghun"},"age":{"S":"50"}})
  
