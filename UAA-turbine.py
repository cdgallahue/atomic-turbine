import requests
import json
import os
import websocket
import time
import urllib2


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

def query_turbine_status(turbine_num):
	tempUrl = 'https://turbine-farm.run.aws-usw02-pr.ice.predix.io/api/turbines/' + str(turbine_num) + '/heartbeat'
	return requests.get(tempUrl).json()
	
def query_turbine_temp(turbine_num):
	tempUrl = 'https://turbine-farm.run.aws-usw02-pr.ice.predix.io/api/turbines/' + str(turbine_num) + '/sensors/temperature'
	return requests.get(tempUrl).json()
	
def query_turbine_volt(turbine_num):
	tempUrl = 'https://turbine-farm.run.aws-usw02-pr.ice.predix.io/api/turbines/' + str(turbine_num) + '/sensors/voltage'
	return requests.get(tempUrl).json()
	
def post_data(timestamp, type, value, turbine_num):
	name = "atomic-turbine" + str(turbine) + "-" + type
	print("Posting to: " + name)
	tempData = [
			[timestamp, value, 3],
				]
	headers = {
		'Authorization': get_uaa_header(),
		'Predix-Zone-Id': zone_id,
		'Content-Type': 'application/json',
			}
	message = {
		"messageId": name + '-' + str(timestamp),
		"body": [
				 {
				 "name": name,
				 "datapoints": tempData
				 }
				 ]
			}
	ws = websocket.create_connection(ingestion_url, header=headers)
	ws.send(json.dumps(message))
	return ws.recv()

#post data

while (1):
	for turbine in [1,2,3]:

        # tempUrl ='https://turbine-farm.run.aws-usw02-pr.ice.predix.io/api/turbines/' + str(turbine) + '/sensors/temperature'
        # ##grab value and assign it to temperature
        # temperature = urllib2.urlopen(tempUrl).read()
        # myArray = temperature.split(':')
        # myValue = myArray[3].split('}')
        # temp = float(myValue[0])
    
        # print('temp')
        # print(temp)
    
    
        # myArray = temperature.split(':')
        # myValue = myArray[1].split(',')
        # tempTime = myValue[0]
        # print('temp time')
        # print(tempTime)
    
    
        # voltUrl ='https://turbine-farm.run.aws-usw02-pr.ice.predix.io/api/turbines/' + str(turbine) + '/sensors/voltage'
            # ##grab value and assign it to voltage
        # voltage = urllib2.urlopen(voltUrl).read()
        # myArray = voltage.split(':')
        # myValue = myArray[3].split('}')
        # volt = float(myValue[0])
    
        # print("volts")
        # print(volt)
    
        # myArray = voltage.split(':')
        # myValue = myArray[1].split(',')
        # vtime = myValue[0]

        # print('volt time')
        # print(vtime)

        # tempData = [
                # [tempTime, temp, 3],
                    # ]
        # headers = {
            # 'Authorization': get_uaa_header(),
            # 'Predix-Zone-Id': zone_id,
            # 'Content-Type': 'application/json',
                # }
        # message = {
            # "messageId": 'atomic-' + str(currTime),
            # "body": [
                     # {
                     # "name": 'atomic-turbine1-temp',
                     # "datapoints": tempData
                     # }
                     # ]
                # }

        # ws = websocket.create_connection(ingestion_url, header=headers)
        # ws.send(json.dumps(message))
        # result = ws.recv()
		currTime = time.time()
		status = query_turbine_status(turbine)["status"]
		print("Turbine " + str(turbine) + " status as of " + str(currTime) + ": " + status)
		s = post_data(currTime, "status", status, turbine)
		print(s)
		volt = query_turbine_volt(turbine)
		temp = query_turbine_temp(turbine)
        if not type(temp) == None:
	        t = post_data(currTime, "temp", temp["value"], turbine)
        if not type(volt) == None:
		    v = post_data(currTime, "volt", volt["value"], turbine)
		print(t)
		print(v)
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
