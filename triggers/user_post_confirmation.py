import json
from domain.user import User
from repository.userDynamoDB import addUser

def create(event, context):
    if 'userName' not in event:
        logging.error("userName attribute does not exist. Validation Failed for request {}".format(event))
        raise Exception("Couldn't create the user.")
    name = event.get("userName")
    request = event.get("request")
    userAttributes = request.get("userAttributes")
    id = userAttributes.get("sub")
    phone_number = userAttributes.get("phone_number")
    email = userAttributes.get("email")
    user= User(id,name,email,phone_number)
    user.id=id
    user.email= email
    user.name = name
    user.mobile=phone_number
    
    return addUser(user)