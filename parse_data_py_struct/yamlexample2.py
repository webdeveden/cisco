import yaml
from yaml import load, load_all

#extract the yaml file
stream = open('sample1.yaml','r')

#parse it to python
documents = load_all(stream, Loader= yaml.FullLoader)

# iterate through out the document
print(type(documents))
for i in documents:
    print()
for a in i['switch']:
    for k, v in a.items():
        #if a['status'] == True:
        print("{}: {}".format(k,v))
    #print(type(k))
    
    
#for k, v in items['switch'].items():
    #print("{}: {}".format(k,v))