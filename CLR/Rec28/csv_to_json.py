import csv 
import json 

def csv_to_json(csvFilePath, jsonFilePath):
    data = {}
    data["label"] = "Recommendation Code List 28"
    data["uri"] = "rec28"
    data["comment"] = "Codes for Types of Means of Transport"
    values = []
      
    #read csv file
    with open(csvFilePath, encoding='utf-8') as csvf: 
        #load csv file data using csv library's dictionary reader
        csvReader = csv.DictReader(csvf) 

        #convert each csv row into python dict
        for row in csvReader: 
            #add this python dict to json array
            row["uri"] = "unece:rec28#"+row["Code-A"]+row["Code-B"]
            values.append(row)
    
    data["values"] = values
    data["referencedBy"] = []
  
    #convert python jsonArray to JSON String and write to file
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf: 
        jsonString = json.dumps(data, indent=4)
        jsonf.write(jsonString)
          
csvFilePath = r'current/code-list.csv'
jsonFilePath = r'current/rec28.json'
csv_to_json(csvFilePath, jsonFilePath)