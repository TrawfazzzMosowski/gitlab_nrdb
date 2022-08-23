
import requests
import gzip
import json


def write_data(in_json, license_key, account_id):

    nrdb_url = 'https://insights-collector.newrelic.com/v1/accounts/'+ account_id + '/events'

    dict_to_json = json.dumps(in_json)
    encoded_json = bytes(dict_to_json, 'UTF-8')
    zipped = gzip.compress(encoded_json)

    headers = {"Content-Type": "application/json", "X-Insert-Key": license_key, "Content-Encoding": "gzip"}
    #print(headers)
    try:
        response = requests.post(nrdb_url, headers=headers, data=zipped)

        print("Status Code", response.status_code)
        return response.status_code
    except Exception as e:
        print(e)
        return 'failed'
