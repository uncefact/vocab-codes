import csv 
import json 

def csv_to_json(csvFilePath, jsonFilePath):
    data = {}
    data["label"] = "Recommendation Code List 23"
    data["uri"] = "rec23"
    data["comment"] = "Freight Cost Code (FCC)"
    values = []
      
    #read csv file
    with open(csvFilePath, encoding='utf-8') as csvf: 
        #load csv file data using csv library's dictionary reader
        csvReader = csv.DictReader(csvf) 

        #convert each csv row into python dict
        for row in csvReader: 
            #add this python dict to json array
            row["uri"] = "unece:rec23#"+row["Group"]+row["Subgroup"]+row["Detail"]
            values.append(row)
    
    data["values"] = values
    data["referencedBy"] = []
  
    #convert python jsonArray to JSON String and write to file
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf: 
        jsonString = json.dumps(data, indent=4)
        jsonf.write(jsonString)
          
csvFilePath = r'current/code-list.csv'
jsonFilePath = r'current/rec23.json'
csv_to_json(csvFilePath, jsonFilePath)