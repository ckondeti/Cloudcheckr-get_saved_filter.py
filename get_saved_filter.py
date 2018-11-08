import requests
import json

apikey_value = ''

def get_detailed_billing_with_grouping_v2(api_key):
    half_url = 'https://api.cloudcheckr.com/api/billing.json/get_detailed_billing_with_grouping_v2'
    api_parameters = {'saved_filter_name': 'Test', 'use_cc_account_id': '68', 'start': '2018-06-01', 'end': '2018-06-30'} 

    resp = requests.get(half_url, params=api_parameters, headers = {"access_key": api_key})
    data = resp.json()
    savedfilterData = data['CostsByGroup']
    return savedfilterData

savedfilterData =  get_detailed_billing_with_grouping_v2(apikey_value)
print(savedfilterData)
