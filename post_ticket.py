##Creating data

import json
import requests

# New ticket info
subject = 'Prueba IGBot!'
body = 'This is the first automatic ticket'

# Package the data in a dictionary matching the expected JSON
data = {'ticket': {'subject': subject, 'comment': {'body': body}}}

# Encode the data to create a JSON payload
payload = json.dumps(data)

# Set the request parameters
url = 'https://ignetworks.zendesk.com/api/v2/tickets.json'
user = 'gcuenya@ignetworks.com'
pwd = 'Chvuoya6'
headers = {'content-type': 'application/json'}

# Do the HTTP post request
response = requests.post(url, data=payload, auth=(user, pwd), headers=headers)

# Check for HTTP codes other than 201 (Created)
if response.status_code != 201:
    print('Status:', response.status_code, 'Problem with the request. Exiting.')
    exit()

# Report success
print('Successfully created the ticket.')
