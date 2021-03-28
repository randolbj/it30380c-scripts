import json
import requests



r = requests.get('http://localhost:3000')

data = r.json()

print(data)

for i in data:
    print (i["name"] + " is = ", end='')
    print (i["color"])


#widet1 is blue..
#widet2 is green.
#widget3 is ....



#dictionaries are in { } and use key value pairs 
#Lists are in [ ] and use numeric indexes [0-n]