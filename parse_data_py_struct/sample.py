import xml.etree.ElementTree as ET # this a built-in xml library in python

#Get the XML file data
stream = open('sample.xml','r')

#Parse the data into an ElementTree object
xml = ET.parse(stream) # ET.parse ,this create an xml variable that is an ElementTree object

#Get the 'root' Element object from the ElementTree
root = xml.getroot() # getroot, returns a root variable, (element object)

#Iterate through each child of the root Element
for e in root:
    #Print the stringified version of the element
    print(ET.tostring(e)) # ET.tostring(), a function that generate a string in representation of XML element
    print("")

    #Print the 'Id' attribute of the Element object
    print(e.get("Id"))
