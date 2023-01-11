import json

respFile = "resp.json"
targetName = "shrank.json"
with open(respFile, "r") as f:
    rawRank = json.load(f)

shrank = []
for item in rawRank:
    shrank.append(
        {   
            "i" : item["id"],
            "r" : item["scientificRank"]["sciRank"] if item["scientificRank"] else None,
        })
    
with open(targetName, "w+") as f:
    f.writelines(json.dumps(shrank , separators=(',', ':')))
