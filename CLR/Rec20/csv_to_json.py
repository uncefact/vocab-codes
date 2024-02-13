import csv 
import json 

def csv_to_json(csvFilePath, jsonFilePath):
    data = {}
    data["label"] = "Recommendation Code List 20"
    data["uri"] = "rec20"
    data["comment"] = "CODES FOR UNITS OF MEASURE USED IN INTERNATIONAL TRADE"
    values = []
      
    #read csv file
    with open(csvFilePath, encoding='utf-8') as csvf: 
        #load csv file data using csv library's dictionary reader
        csvReader = csv.DictReader(csvf) 

        #convert each csv row into python dict
        for row in csvReader: 
            #add this python dict to json array
            row["uri"] = "unece:rec20#"+row["CommonCode"]
            values.append(row)
    
    data["values"] = values
    data["referencedBy"] = []
  
    #convert python jsonArray to JSON String and write to file
    with open(jsonFilePath, 'w', encoding='utf-8') as jsonf: 
        jsonString = json.dumps(data, indent=4)
        jsonf.write(jsonString)
          
csvFilePath = r'current/Annex || & Annex |||/code-list.csv'
jsonFilePath = r'current/rec20.json'
csv_to_json(csvFilePath, jsonFilePath)