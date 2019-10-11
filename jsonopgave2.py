import json
from urllib import request

url = "https://jsonplaceholder.typicode.com/users"
id = input("geef een id op: ")
url += "?id="+id

result = request.urlopen(url)
#inhoud = result.read().decode("utf8")
data = json.load(result)[0] # het eerste (en enige) element van de list
print("\nruwe data: ", data)
print("\nnaam, email en telefoon:")
print(data["name"])
print(data["email"])
print(data["phone"])


