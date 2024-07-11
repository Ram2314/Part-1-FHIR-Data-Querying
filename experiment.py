import requests

# Patient id
id = 'X12984'

# Patient id
id = 'X12984'

# Base URL
base_url = 'http://fhirserver.hl7fundamentals.org/fhir'
resource = 'Goal'

# Parameters for the request
params = {
    "patient": id,
    "_format": "json",
}

# Construct the request URL
observation_request = f"{base_url}/{resource}"

# Print the request URL for debugging purposes
print('Now Searching for Goal...@', observation_request)

# Perform the request with parameters
response = requests.get(observation_request, params=params)
goal_response = response.json()

for goal_resource in goal_response['entry']:
    effectiveDateTime = goal_resource['resource']['effectiveDateTime']
    text = goal_resource['resource']['code']['text']
    value_unit = f"{goal_resource['resource']['valueQuantity']['value']} {goal_resource['resource']['valueQuantity']['unit']}"
    print(f"{effectiveDateTime} | {text} | {value_unit}")
print()


