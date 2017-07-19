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

def count_outages_from_query(status_query_results):
	outage_count = 0
	i = 0
	while i < len(status_query_results):
		result = status_query_results[i]
		if result[1] == "OFFLINE":
			outage_duration = find_outage_length(status_query_results, i)
			if outage_duration >= 3:
				outage_count += 1
			i += outage_duration - 1
		i += 1
	return outage_count

def find_outage_length(status_query_results, start_index):
	i = start_index
	while status_query_results[i][1] == "OFFLINE":
		i += 1
	return i

sq1 = get_results_from_query(query_tsdb("24h-ago", 1, "status"))
sq2 = get_results_from_query(query_tsdb("24h-ago", 2, "status"))
sq3 = get_results_from_query(query_tsdb("24h-ago", 3, "status"))
vq1 = get_results_from_query(query_tsdb("24h-ago", 1, "volt"))
vq2 = get_results_from_query(query_tsdb("24h-ago", 2, "volt"))
vq3 = get_results_from_query(query_tsdb("24h-ago", 3, "volt"))
tq1 = get_results_from_query(query_tsdb("24h-ago", 1, "temp"))
tq2 = get_results_from_query(query_tsdb("24h-ago", 2, "temp"))
tq3 = get_results_from_query(query_tsdb("24h-ago", 3, "temp"))
print(sq1)
print(sq2)
print(sq3)
print("\n")
#print(count_outages_from_query(sq1))
#print(count_outages_from_query(sq2))
#print(count_outages_from_query(sq3))
print("\n")
print(vq1)
print(vq2)
print(vq3)
print("\n")
print(tq1)
print(tq2)
print(tq3)
print("\n")