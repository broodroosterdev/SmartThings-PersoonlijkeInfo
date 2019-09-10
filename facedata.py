import json
import mysql.connector as mariadb
import os, sys
sys.path.append(os.path.realpath(__file__))
import userdata

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

print(getDataById(1))
mydata = userdata.User(klassen=["ICTM1o", "ICTM!o3"])
print(mydata.getSerialized())