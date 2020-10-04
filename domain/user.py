from shared.domain_model import DomainModel

class User(object):
    def __init__(self, id, name, email, mobile, age= None,gender = None, liking = None):
        self.id = id
        self.name = name
        self.email = email
        self.mobile = mobile
        self.age = age
        self.gender = gender
        self.liking = liking

    def __eq__(self, other):
        return self.to_dict() == other.to_dict()


DomainModel.register(User)