import json
import mysql.connector as mariadb
import os, sys
sys.path.append(os.path.realpath(__file__))
import userdata
import nextTrain

maria_config = {};
with open('config.json') as json_data:
    maria_config = json.load(json_data)
    json_data.close()
print(maria_config);
mariadb_connection = mariadb.connect(
    user=maria_config['user'],
    password=maria_config['password'],
    database=maria_config['database'])

def getDataById(id):
    return getJson("SELECT * FROM userdata WHERE user_id='%s'" % id)

def getJson(query):
    cursor = mariadb_connection.cursor()
    cursor.execute(query)
    field_names = [i[0] for i in cursor.description]
    # returned rows (tuples)
    rows = cursor.fetchall()
    # close cursor and database
    cursor.close()
    data = []
    for row in rows:
        data.append(dict(zip(field_names, row)))
    return data

def setJson(query):
    cursor = mariadb_connection.cursor()
    cursor.execute(query)
    mariadb_connection.commit()
    cursor.close()

def updateJson(user, id):
    setJson("UPDATE userdata SET data='{}' WHERE user_id={}".format(user.getSerialized(), id))

def updateUser(user):
    setJson("UPDATE userdata SET first_name='{}', last_name='{}', age='{}', postal_code='{}', city='{}', data='{}' WHERE user_id='{}'".format(
        user.first_name,
        user.last_name,
        user.age,
        user.postal_code,
        user.city,
        json.dumps(user.data),
        user.user_id
    ))

def dataToUser(data):
    return userdata.User(user_data=data)

def getVertrekTijdenById(id):
    user = dataToUser(getDataById(2)[0])
    print(json.dumps(user.data))
    return nextTrain.getVertrekTijden(user.data["richting"])


print(getVertrekTijdenById(4))
    #print(json.dumps(user.data))
#print(nextTrain.getVertrekTijden(user.data['richting']))