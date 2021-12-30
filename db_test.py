import pymongo


client = pymongo.MongoClient("mongodb+srv://admin:pass@cluster0.orrpa.mongodb.net/INR_Data?ssl=true&ssl_cert_reqs=CERT_NONE",connect=False)
#db = client.Criteria
#",connect=False)
db = client.INR_Data
coll = db.INR_Data
data=coll.find({"Unmissable":1})
print(data)