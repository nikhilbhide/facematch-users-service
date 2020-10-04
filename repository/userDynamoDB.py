from domain.user import User
import boto3
import json 

dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table("users")


''' Add user to the datastore with id, name, email and mobile_number attributes.
This is done using a trigger right after user sign up confirmation.
Here only basic attributes are available.
Upon login, user is supposed to update the info.'''
def addUser(user:User):
    item = {
        'id': user.id,
        'name': user.name,
        'email': user.email,
        'mobile_number': user.mobile
    }

    # write the todo to the database
    table.put_item(Item=item)

    # create a response
    response = {
        "statusCode": 200,
        "body": json.dumps(item)
    }

    return response

''' Update the extended user attributes for the existing userid'''
def updateUser(user:User):
    response = table.update_item(
        Key={
            'id': user.id
        },
        UpdateExpression="set age=:a, gender=:g, liking=:l, email=:e, mobile_number=:m",
        ExpressionAttributeValues={
            ':a': user.age,
            ':g': user.gender,
            ':l': user.liking,
            ':e': user.email,
            ':m': user.mobile
        },
        ReturnValues="UPDATED_NEW"
    )
    return response

'''Retrieve the user by id'''
def getUserById(id):
    try:
        response = table.get_item(Key={'id': id})
    except ClientError as e:
        print(e.response['Error']['Message'])
    else:
        return response['Item']