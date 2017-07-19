import requests
import json
import os
import websocket
import time
import urllib2
#import psycopg2


def get_uaa_header():
    return 'Bearer ' + access_token
    
#url = os.environ['UAA_URI']
url = 'https://ff2359d6-05b4-4a0f-9001-2533c77cfe9d.predix-uaa.run.aws-usw02-pr.ice.predix.io/oauth/token'

payload = "grant_type=client_credentials"
headers = {
    'content-type': "application/x-www-form-urlencoded",
#    'authorization': os.environ['UAA_Authorization']
    'authorization': 'Basic dHMtY2xpZW50MTpLZld1cHhTd001Q1hmaDg='
    }

response     = requests.request("POST", url, data=payload, headers=headers)
access_token = json.loads(response.text)[u'access_token']

#print(access_token)


#zone_id = os.getenv('TS_PREDIX_ZONE_ID')
#ingestion_url = os.getenv('TIMESERIES_INGESTION_URL')
#query_url = os.getenv('TS_QUERY_URL')
zone_id = 'd97f5953-2c07-4e8f-ac0d-8b8df897135e'
ingestion_url = 'wss://gateway-predix-data-services.run.aws-usw02-pr.ice.predix.io/v1/stream/messages'
query_url = 'https://time-series-store-predix.run.aws-usw02-pr.ice.predix.io/v1/datapoints'

currTime = int(round(time.time()))

def query_turbine_status(turbine_num):
    tempUrl = 'https://turbine-farm.run.aws-usw02-pr.ice.predix.io/api/turbines/' + str(turbine_num) + '/heartbeat'
    return requests.get(tempUrl).json()
    
def query_turbine_temp(turbine_num):
    tempUrl = 'https://turbine-farm.run.aws-usw02-pr.ice.predix.io/api/turbines/' + str(turbine_num) + '/sensors/temperature'
    myArry = requests.get(tempUrl).json()   
    return myArry
    
def query_turbine_volt(turbine_num):
    tempUrl = 'https://turbine-farm.run.aws-usw02-pr.ice.predix.io/api/turbines/' + str(turbine_num) + '/sensors/voltage'
    myArry = requests.get(tempUrl).json()   
    return myArry
    
def post_data(timestamp, type, value, turbine_num):
    tempData = [
            [timestamp, value, 3],
                ]
    headers = {
        'Authorization': get_uaa_header(),
        'Predix-Zone-Id': zone_id,
        'Content-Type': 'application/json',
            }
    message = {
        "messageId": 'atomic-' + type + '-' + str(timestamp),
        "body": [
                 {
                 "name": 'atomic-turbine' + str(turbine_num) + '-' + type,
                 "datapoints": tempData
                 }
                 ]
            }
    ws = websocket.create_connection(ingestion_url, header=headers)
    ws.send(json.dumps(message))
    return ws.recv()

#post data

#try:
    #conn = psycopg2.connect(dbname='energystream', user='johndwyer', host='localhost', password='')
    #conn.autocommit = True
#except:
    #print("i could not connect")
    #sys.exit()
#cur = conn.cursor()

while (1):
    for turbine in [1, 2, 3]:
        currTime = time.time()
        status = query_turbine_status(turbine)["status"]
        #print("Turbine " + str(turbine) + " status as of " + str(currTime) + ": " + status)
        post_data(currTime, "status", status, turbine)
        if status == "ONLINE":
            volt = query_turbine_volt(turbine)#["voltage"]
            temp = query_turbine_temp(turbine)#["temperature"]
            if not type(temp) is None:
                post_data(currTime, "temp", temp["value"], turbine)
            else:
                post_data(currTime, "temp", 0, turbine)
            if not type(volt) is None:
                post_data(currTime, "volt", volt["value"], turbine)
            else:
                post_data(currTime, "volt", 0, turbine)
            print("Turbine: " + str(turbine) + " Time: " + str(currTime) + " Status: " + status)
        else:
            print("Turbine: " + str(turbine) + " Time: " + str(currTime) + " Status: " + status)
            #insert = "INSERT INTO energystream (voltage, time, temp, heartbeat, turbineid) VALUES ('" + str(volt) + "', '" + str(currTime) + "', '" + str(temp) + "', '" + str(status) + "', " + str(turbine) + ");"
            #cur.execute(insert)
    time.sleep(3)
        
#print('Got back message confirmation TimeSeries:\n %s' % result)


#get data

headers = {
    'Authorization': get_uaa_header(),
    'Predix-Zone-Id': zone_id
}
body = {
    "start": 10,
    "tags": [
        {
            "name": 'atomic-turbine1-temp'
        }
    ]
}
response = requests.post(query_url, headers=headers, data=json.dumps(body))

print(response.json())
