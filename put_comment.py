import json
import requests

# Ticket to update
id = '103'
body = 'Thanks for choosing Acme Jet Motors.'

# Package the data in a dictionary matching the expected JSON
data = { 'ticket': { 'comment': { 'body': body } } }

# Encode the data to create a JSON payload
payload = json.dumps(data)

# Set the request parameters
url = 'https://your_subdomain.zendesk.com/api/v2/tickets/' + id + '.json'
user = 'your_email_address'
pwd = 'your_password'
headers = {'content-type': 'application/json'}

# Do the HTTP put request
response = requests.put(url, data=payload, auth=(user, pwd), headers=headers)

# Check for HTTP codes other than 200
if response.status_code != 200:
    print('Status:', response.status_code, 'Problem with the request. Exiting.')
    exit()

# Report success
print('Successfully added comment to ticket #{}'.format(id))
