

import json
import requests
import time
import urllib2
import psycopg2
import sys
from psycopg2 import sql
#import websocket



def checkURL(URL):
    request = requests.get(URL)
    if request.status_code == 200:
        return True
    else:
        return False


def getTemp(turbine):
    url ='https://turbine-farm.run.aws-usw02-pr.ice.predix.io/api/turbines/' + str(turbine) + '/sensors/temperature'
    ##grab value and assign it to temperature
    if checkURL(url):
        temperature = urllib2.urlopen(url).read()
        if temperature == '{}':
            return 'SensorError'
        myArray = temperature.split(':')
        myValue = myArray[3].split('}')
        return float(myValue[0])
    else:
        return 'SensorError'

def getVoltage(turbine):
    str(turbine)
    url ='https://turbine-farm.run.aws-usw02-pr.ice.predix.io/api/turbines/' + str(turbine) + '/sensors/voltage'
    ##grab value and assign it to voltage
    if checkURL(url):
        voltage = urllib2.urlopen(url).read()
        if voltage == '{}':
            return 'SensorError'
        myArray = voltage.split(':')
        myValue = myArray[3].split('}')
        return float(myValue[0])
    else:
        return 'SensorError'

def getHeartBeat(turbine):
    url = 'https://turbine-farm.run.aws-usw02-pr.ice.predix.io/api/turbines/' + str(turbine) + '/heartbeat'
    if checkURL(url):
        heartbeat = urllib2.urlopen(url).read()
        if heartbeat == '{}':
            return 'OFFLINE'
        myArray = heartbeat.split(':')
        size = len(myArray)
        cleanResult = myArray[size-1].split("\"")
        return cleanResult[1]
    else:
        return 'SensorError'

def getTimeStamp(turbine):
    url ='https://turbine-farm.run.aws-usw02-pr.ice.predix.io/api/turbines/' + str(turbine) + '/sensors/temperature'
    ##grab value and assign it to voltage
    if checkURL(url):
        voltage = urllib2.urlopen(url).read()
        if voltage == '{}':
            return ''
        myArray = voltage.split(':')
        myValue = myArray[1].split(',')
        return myValue[0]
    else:
        return 'SensorError'


#headers = {'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsImtpZCI6ImxlZ2FjeS10b2tlbi1rZXkiLCJ0eXAiOiJKV1QifQ.eyJqdGkiOiI3NzUzZjZhNWFjNTc0ZjFmODc1YTIwNzM0Y2U5MTlmZSIsInN1YiI6InRzLWNsaWVudDEiLCJzY29wZSI6WyJ1YWEucmVzb3VyY2UiLCJ0aW1lc2VyaWVzLnpvbmVzLmQ5N2Y1OTUzLTJjMDctNGU4Zi1hYzBkLThiOGRmODk3MTM1ZS5pbmdlc3QiLCJ1YWEubm9uZSIsInRpbWVzZXJpZXMuem9uZXMuZDk3ZjU5NTMtMmMwNy00ZThmLWFjMGQtOGI4ZGY4OTcxMzVlLnVzZXIiLCJ0aW1lc2VyaWVzLnpvbmVzLmQ5N2Y1OTUzLTJjMDctNGU4Zi1hYzBkLThiOGRmODk3MTM1ZS5xdWVyeSJdLCJjbGllbnRfaWQiOiJ0cy1jbGllbnQxIiwiY2lkIjoidHMtY2xpZW50MSIsImF6cCI6InRzLWNsaWVudDEiLCJncmFudF90eXBlIjoiY2xpZW50X2NyZWRlbnRpYWxzIiwicmV2X3NpZyI6IjlkYWMxM2ZmIiwiaWF0IjoxNTAwMDU1NDUyLCJleHAiOjE1MDAwOTg2NTIsImlzcyI6Imh0dHBzOi8vZmYyMzU5ZDYtMDViNC00YTBmLTkwMDEtMjUzM2M3N2NmZTlkLnByZWRpeC11YWEucnVuLmF3cy11c3cwMi1wci5pY2UucHJlZGl4LmlvL29hdXRoL3Rva2VuIiwiemlkIjoiZmYyMzU5ZDYtMDViNC00YTBmLTkwMDEtMjUzM2M3N2NmZTlkIiwiYXVkIjpbInRpbWVzZXJpZXMuem9uZXMuZDk3ZjU5NTMtMmMwNy00ZThmLWFjMGQtOGI4ZGY4OTcxMzVlIiwidWFhIiwidHMtY2xpZW50MSJdfQ.r8QqCe3OW_oz4EnUh5BiUFbL9Dy0fXwQ0l1-sfPBQmCnk5ZzlYpVbp_xBDgU-hfLIaZyJE_COTe7fV73gfi7I9pk49Ravq_pnSYxFN4ed3G7QsPw4WjJyb07wIYeaEfZv4EsOU6xwWVms86nIF4mq0pRC_dTIPNXt66SN9C3GR9xfgGqd_x8f4t4onEIAUQ10tRImaLW2_Yb7c19PHK3dENLD5p4dXswCP5sBRlAbV9oA37rAbzgpaGOeLbQWe21w1PQ3sHwmxoLYBdDnZDizoWZa1mcOf1tcKCdHVXSxDZQKCdIY_fOLAB93K1-iqfAWOD2944ck2rkfMDa5vJq1g','Predix-Zone-Id': 'd97f5953-2c07-4e8f-ac0d-8b8df897135e'}
#Payload:
#{"start": 1500051600000,"end": 1500058800000,"tags": [{"name": "Atomice-turbine-1-Temperature", "filters":{ "quality": 2}}]


#ingestionUrl = 'https://gateway-predix-data-services.run.aws-usw02-pr.ice.predix.io/v1/stream/messages'

#while (1):
#    for i in [1,2,3]:
#        for variable in ['Temperature','Voltage','Time','Heartbeat']:
#            myString = 'Atomic-turbine-' + str(i) + '-' + variable
#            data = {'messageID': 'Atomic-[]','body': [{'name': myString,'datapoints': [[getTimeStamp(i),getTemp(i),2]]}]}

#data = {'messageID': 'Atomic-[]','body': [{'name': 'Atomice-turbine-1-Temperature','datapoints': [[getTimeStamp(1),getTemp(1),2]]}]}
#r = requests.get(ingestionUrl, data=json.dumps(data), headers=headers)
#print(r)


#{"start": 1500051600000,"end": 1500058800000,"tags": [{"name": "Atomic-turbine-1-Temperature"}], "quality": 2}#,"limit": 1000,"aggregations": [{"type": "avg","interval": "1h"}],"filters": {"attributes": {"host": "<host>","type": "<type>"},"measurements": {"condition": "ge","values": "23.1"},"qualities": {"values": ["0","3"]}}}]}
#time.sleep(10)

#print('Thanks for playing')




while (1):
    try:
        conn = psycopg2.connect(dbname='energystream', user='johndwyer', host='localhost', password='')
        conn.autocommit = True
    except:
        print("i could not connect")
        sys.exit()
    cur = conn.cursor()
    #print voltage of each turbine
    for i in [1, 2, 3]:
        turbineid = i
        voltage = getVoltage(i)
        temp = getTemp(i)
        heartbeat = getHeartBeat(i)
        timestamp = getTimeStamp(i)
        print('turbine {0}: Voltage->{1} -- Temperature->{2} -- Heartbeat->{3} -- Timestamp->{4}'.format(i, voltage, temp, heartbeat, timestamp))
        insert = "INSERT INTO energystream (voltage, time, temp, heartbeat, turbineid) VALUES ('" + str(voltage) + "', '" + str(timestamp) + "', '" + str(temp) + "', '" + str(heartbeat) + "', " + str(i) + ");"
        cur.execute(insert)
    time.sleep(10)
cur.close()


#use .datetime.fromtimestamp(ms/1000) to get date formate
## wait 2 seconds before printing again




