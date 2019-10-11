import json
from urllib import request
url = "https://jsonplaceholder.typicode.com/users"
id = input("geef een id op: ")
url += "?id="+id
result = request.urlopen(url)
data = json.load(result)[0]
print(data["name"])
print(data["email"])
print(data["phone"])

