
myObj = {"people": 
[
    {
       "Id": 1,
       "FirstName": "Benjamin",
       "LastName": "Finkel",
       "Email": "ben.finkel@cbtnuggets.com",
       "Active" : true
    },
    {
       "Id": 2,
       "Name": ["Jane", "Doe"],
       "Email": "jane.doe@cbtnuggets.com",
       "Active" : false
    },
    {
       "Id": 3,
       "FirstName": "Pat",
       "LastName": "Smith",
       "Email": "pat.smith@cbtnuggets.com",
       "Active" : true
    }
 ]}
 
 
 console.log(typeof myObj.people[2].Id); // getting the type of an element
 