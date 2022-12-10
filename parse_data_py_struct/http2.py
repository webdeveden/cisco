import json

stream = json.load(open('http2.json'))

#print(type(stream))

for k,v in stream.items():
    print("{}: {}".format(k,v),end="\n")