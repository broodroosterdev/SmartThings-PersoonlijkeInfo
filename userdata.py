import json
class User:
    data = {}
    data['klascodes'] = [];
    def __init__(self, klassen):
        for klas in klassen:
            self.data['klascodes'].append(klas);
    def getSerialized(self):
        return json.dumps(self.data)