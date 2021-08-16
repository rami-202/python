import urllib.request as ur
import json

# json_url = 'http://python-data.dr-chuck.net/comments_42.json'

j_url = input("Enter location: ")
print("Retrieving ", j_url)
data = ur.urlopen(j_url).read().decode('utf-8')
print('Retrieved', len(data), 'characters')
j_obj = json.loads(data)

sum = 0
total_number = 0

for comment in j_obj["comments"]:
    sum += int(comment["count"])
    total_number += 1

print('Count:', total_number)
print('Sum:', sum)
