import json
def jsonDefault(OrderedDict):
    return OrderedDict.__dict__

class User:
    user_id = 0
    first_name = "";
    last_name = "";
    age = 0;
    postal_code = "";
    city = ""
    data = {}

    def __init__(self, klassen=[], user_data={}):
        if (user_data != {}):
            self.user_id = user_data['first_name']
            self.first_name = user_data['first_name']
            self.last_name = user_data['last_name']
            self.age = user_data['age']
            self.postal_code = user_data['postal_code']
            self.city = user_data['city']
            self.data = json.loads(user_data['data'])
            return
        # for klas in klassen:
        #    self.data['klascodes'].append(klas);

    def __repr__(self):
        return json.dumps(self, default=jsonDefault, indent=4)
    #def getSerialized(self):
    #    jsonUser = "{ 'user_id': '{0}', 'first_name': '{1}', 'last_name': '{2}', 'age': {3}, 'postal_code': '{4}'," \
    #               "'city': '{5}','data': '{6}'}".format(
    #        self.user_id,
    #       self.first_name,
    #        self.last_name,
    #        self.age,
    #        self.postal_code,
    #        self.city,
    #        self.data
    #    )
    #    return json.dumps(json.loads(jsonUser))

