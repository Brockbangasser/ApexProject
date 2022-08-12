import requests
import json
originName = "brockb123456"
response = requests.get("https://api.mozambiquehe.re/bridge?auth=6f012a775e58394b4caf8496a29509fc&player=" + originName
                        + "&platform=PC")
# turns response object into string and then to a python object
pyObject = json.loads(response.text)
# turns the python object into a string with the result of the JSON serialization process
responseString = json.dumps(pyObject)