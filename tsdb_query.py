import requests
import json
import os
import websocket
import time
import urllib2

zone_id = 'd97f5953-2c07-4e8f-ac0d-8b8df897135e'
query_url = 'https://time-series-store-predix.run.aws-usw02-pr.ice.predix.io/v1/datapoints'
	
url = 'https://ff2359d6-05b4-4a0f-9001-2533c77cfe9d.predix-uaa.run.aws-usw02-pr.ice.predix.io/oauth/token'

payload = "grant_type=client_credentials"
headers = {
	'content-type': "application/x-www-form-urlencoded",
	'authorization': 'Basic dHMtY2xpZW50MTpLZld1cHhTd001Q1hmaDg='
	}

response     = requests.request("POST", url, data=payload, headers=headers)
access_token = json.loads(response.text)[u'access_token']

#start should either be a number for an absolute time in milliseconds, or a string formatted for relative time
def query_tsdb(start, turbine_num, type):
	headers = {
		'Authorization': 'Bearer ' + access_token,
		'Predix-Zone-Id': zone_id
	}
	body = {
		"start": start,
		"tags": [
			{
				"name": 'atomic-turbine' + str(turbine_num) + '-' + type
			}
		]
	}
	return requests.post(query_url, headers=headers, data=json.dumps(body))

def get_results_from_query(query_result):
	return query_result.json()["tags"][0]["results"][0]["values"]
	
print(get_results_from_query(query_tsdb(10, 1, "status")))
print(get_results_from_query(query_tsdb(10, 1, "volt")))
print(get_results_from_query(query_tsdb(10, 1, "temp")))
print("\n")
print(get_results_from_query(query_tsdb(10, 2, "status")))
print(get_results_from_query(query_tsdb(10, 2, "volt")))
print(get_results_from_query(query_tsdb(10, 2, "temp")))
print("\n")
print(get_results_from_query(query_tsdb(10, 3, "status")))
print(get_results_from_query(query_tsdb(10, 3, "volt")))
print(get_results_from_query(query_tsdb(10, 3, "temp")))
print("\n")