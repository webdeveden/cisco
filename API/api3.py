# this code use Music public API  called discogs by sorting images depending on their types
import json

stream = json.load(open('api2.json'))

print(type(stream))
#print(type(stream['images'][0]))
#print(type(stream['sublabels'][0]))
#print(len(stream['images']))

for k, v in stream.items():
    #print(type(stream[k]))
    if type(stream[k]) == list():
        dic = stream[k][0]
        for i,a in dic.items():
            print("{}: {}".format(i,a))
    else:
        print("{}: {}".format(k,v))