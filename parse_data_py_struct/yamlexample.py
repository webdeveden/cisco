import yaml
from yaml import load, load_all

stream = open('sample.yaml','r')
documents = load_all(stream, Loader=yaml.FullLoader)

#print(type(documents))

for doc in documents:
    #print(type(doc['people']))
    for i in doc['people']:
        for k,v in i.items():
            print("{}: {}".format(k,v))
    



    