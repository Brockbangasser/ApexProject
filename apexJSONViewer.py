import requests
import pyjsonviewer
import json

response = requests.get("https://api.mozambiquehe.re/bridge?auth=6f012a775e58394b4caf8496a29509fc&player=brockb123456"
                        "&platform=PC")
# turns response object into string and then to a python object
pyObject = json.loads(response.text)
# turns the python object into a string with the result of the JSON serialization process
responseString = json.dumps(pyObject)

# turns response into dictionary
# response_dict = response.json()
# print(responseString)
# print(response_dict['global'])
# print(response_dict())

#with open('apex.json', 'w', encoding='utf-8') as json_file:
    #json.dump(responseString, json_file, ensure_ascii=False, indent=4)
print(pyObject)
pyjsonviewer.view_data(json_data=pyObject)
