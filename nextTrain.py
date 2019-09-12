import json
import requests
import datetime
url = "http://127.0.0.1:4000/"
def getVertrekTijden(richting):
    now = datetime.datetime.utcnow() # <-- get time in UTC
    headers = {
        'tijd': now.isoformat("T"),
        'station': 'ZL',
        'richting': richting,
    }
    times = []
    r = requests.get(url, headers=headers);
    for departure in r.json():
        datetime_object = datetime.datetime.strptime(departure['plannedDateTime'].split('+', 1)[0], '%Y-%m-%dT%H:%M:%S')
        times.append("{}:{} op spoor {}".format(datetime_object.hour, datetime_object.minute, departure['plannedTrack']))
    return times
