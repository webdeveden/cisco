# this code use Music public API  called discogs by sorting images depending on their types
import json

stream = json.load(open('api2.json'))

#print(type(stream))
#print(type(stream['images'][0]))
#print(type(stream['sublabels'][0]))
#print(len(stream['images']))
count = 0

for i in stream['images']:
    
    for k,v in i.items():
        if i['type'] == 'secondary':
            count+=1
            print("{}:  {} ".format(k,v))
print("Total equals: {}".format(count))
        