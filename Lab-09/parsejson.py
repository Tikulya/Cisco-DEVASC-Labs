
import json
import yaml

# Open and read the JSON file
with open('myfile.json', 'r') as json_file:
    ourjson = json.load(json_file)

# Display all JSON data
print(ourjson)

# Display selected values
print("The access token is: {}".format(ourjson['access_token']))
print("The token expires in {} seconds.".format(ourjson['expires_in']))

# Convert JSON data to YAML
print("\n\n---")
print(yaml.dump(ourjson))
