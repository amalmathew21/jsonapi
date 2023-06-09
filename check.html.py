import http.client
import json

conn = http.client.HTTPSConnection("jsonexample.onrender.com")

# Data to be passed in the payload
data = {
    "name": "Amal Mathew",
    "age": 23,
    "email": "amal@gmail.com"
}

# data = {
#     "json_file":
#     [
# 	{
# 		"color": "white",
# 		"value": "#002"
#     },
#     {
# 		"color": "yellow",
# 		"value": "#006"
#     },
#     {
# 		"color": "yellow",
# 		"value": "#006"
#     },
#     {
# 		"color": "yellow",
# 		"value": "#006"
#     },{
# 		"color": "black",
# 		"value": "#005"
#     },{
# 		"color": "yellow",
# 		"value": "#006"
#     },{
# 		"color": "red",
# 		"value": "#007"
#     }
#     ]
# }


# Convert the data to JSON format
payload = json.dumps(data)

headers = {
  'Content-Type': 'application/json'
}

conn.request("POST", "/api/json-file/", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))