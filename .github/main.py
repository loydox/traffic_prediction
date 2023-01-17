url = 'https://ussouthcentral.services.azureml.net/workspaces/4ccea4f573b743b3bb748f6bca791cb8/services/0c654a99b93d47b194caf3161c1941cd/execute?api-version=2.0&format=swagger'
api_key = 'Cf7gPgS7yjduvNrvhctmqswT6vORLp15zcH1j69FjhqXLI4GCmhwNIJj3jDAdjOrQrkWLmzN871Z+AMCmkxdGQ==' # Replace this with the API key for the web service

import urllib.request
import json

data = {
        "Inputs": {
                "input1":
                [
                    {
                            'REGION_ID': "1",   
                            'isWeekend': "false",   
                            'BUS_COUNT': "1",   
                            'HOUR': "1",   
                            'DAY_OF_WEEK': "1",   
                            'MONTH': "1",   
                    }
                ],
        },
    "GlobalParameters":  {
    }
}

body = str.encode(json.dumps(data))


headers = {'Content-Type':'application/json', 'Authorization':('Bearer '+ api_key)}

req = urllib.request.Request(url, body, headers)

try:
    response = urllib.request.urlopen(req)

    result = response.read()
    print(result)
except urllib.error.HTTPError as error:
    print("The request failed with status code: " + str(error.code))

    # Print the headers - they include the requert ID and the timestamp, which are useful for debugging the failure
    print(error.info())
    print(json.loads(error.read().decode("utf8", 'ignore')))