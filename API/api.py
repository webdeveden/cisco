import json

stream = json.load(open('api.json'))

#print(type(stream))

for k,v in stream.items():
    print("{}: \n {}".format(k,v))
    
    
        

