import csv 
import json 

def csv_to_json(csvFilePath, jsonFilePath):
    data = {}
    data["label"] = "Recommendation Code List 24"
    data["uri"] = "rec24"
    data["comment"] = "Trade and Transport Status Codes"
    values = []
      
    #read csv file
    with open(csvFilePath, encoding='utf-8') as csvf: 
        #load csv file data using csv library's dictionary reader
        csvReader = csv.DictReader(csvf) 

        #convert each csv row into python dict
        for row in csvReader: 
            #add this python dict to json array
            row["uri"] = "unece:rec24#"+row["Code"]
            values.append(row)
    
    data["values"] = values
    data["referencedBy"] = []
  
    #convert python jsonArray to JSON String and write to file
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf: 
        jsonString = json.dumps(data, indent=4)
        jsonf.write(jsonString)
          
csvFilePath = r'current/code-list.csv'
jsonFilePath = r'current/rec24.json'
csv_to_json(csvFilePath, jsonFilePath)