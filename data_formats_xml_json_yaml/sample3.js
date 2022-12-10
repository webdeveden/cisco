// creating an object inside an object
myObj = {"people": 
[
    {
       "Id": 1,
       "Name": ["Benjamin", "Finkel"],
       "Email": "ben.finkel@cbtnuggets.com",
       "Active" : true
    },
    {
       "Id": 2,
       "Name": ["Jane", "Doe"], // object inside and object using an array
       "Email": "jane.doe@cbtnuggets.com",
       "Active" : false
    },
    {
       "Id": 3,
       "Name": ["Pat", "Smith"],
       "Email": "pat.smith@cbtnuggets.com",
       "Active" : true
    }
 ]}
 
 
 console.log(typeof myObj.people[1].Name); // getting the type of an element
 