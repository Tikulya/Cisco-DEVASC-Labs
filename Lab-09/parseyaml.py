
import json
import yaml

# Read YAML file
with open('myfile.yaml', 'r') as yaml_file:
    ouryaml = yaml.safe_load(yaml_file)

# Display parsed data
print(ouryaml)

# Display selected values
print("The access token is {}".format(ouryaml['access_token']))
print("The token expires in {} seconds.".format(ouryaml['expires_in']))

# Convert YAML to JSON
print("\n\n")
print(json.dumps(ouryaml, indent=4))
