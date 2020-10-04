import json
from domain.user import User
from repository.userDynamoDB import updateUser, getUserById
import sys
from shared.decimalencoder import DecimalEncoder

''' updates user by id '''
def put(event, context):
    try:
        id = event['pathParameters']['id']
        data = json.loads(event['body'])

        # create new user object with extended attributes
        email = data.get("email")
        age = data.get("age")
        name = data.get("name")
        liking = data.get("liking")
        mobile = data.get("mobile")
        gender = data.get("gender")
        user = User(id, name, email, mobile, age, gender, liking)

        # update user in datastore by id
        response = updateUser(user)
        return {
            "statusCode": 200,
            "body":json.dumps("user successfull updated")
        }
    except Exception as e:
        return {
            "statusCode": 500,
            "body": json.dumps("error in processing request")
        }

''' retrieves the user attributes by id '''
def getById(event, context):
    try:
        id = event['pathParameters']['id']

        # update user in datastore by id
        response = getUserById(id)
        print(response)
        return {
            "statusCode": 200,
            "body": json.dumps(response,cls=DecimalEncoder)
        }
    except Exception as e:
        print(e)
        return {
            "statusCode": 404,
            "body": json.dumps("user not found")
        }
