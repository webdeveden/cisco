import json

jsonstr = """{"people":[{"Id":"1","FirstName":"Benjamin","LastName":"Finkel",
    "Email":"ben.finkel@cbtnuggets.com"},{"Id":"2","FirstName":"Jane","LastName":"Doe",
    "Email":"jane.doe@cbtnuggets.com"},{"Id":"3","FirstName":"Pat","LastName":"Smith",
    "Email":"pat.smith@cbtnuggets.com"}]}"""

jsonobj = json.loads(jsonstr)
# json.loads( stand for load string),Pass it in that JSON string, and it brings it into JSON object

#print(jsonobj['people'][1])

jsonobj = json.load(open('sample.json'))

#print(type(jsonobj))
#print(type(jsonobj['people'][1])

for i in jsonobj['people']:
    for k, v in i.items():
        print("{}: {}".format(k,v))
