import json 

#stream = open('http.json')

jsonstr = json.load(open('http.json'))

print(type(jsonstr['people'][0]))

for k, v in jsonstr['people'][0].items():
    print("{}: {}".format(k,v))