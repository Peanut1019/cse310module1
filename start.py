import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

#Get Credentials
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)
#Make sure firebase is initalized
print("Firebase initialized successfully!")

db = firestore.client()
doc_ref = db.collection('module1')
#Read Data
results = db.collection("module1").get()
for result in results:
    print(result.to_dict())
#Data for Creation:
data = {
        "favorite": "pod5",
        "name": "Fname",
        "recent": {
            "hey": "heypod2",
            "ghey": "gheypod2"
        }
}
#Create Data
db.collection("module1").document("567").set(data)

#Update Data
db.collection("module1").document("585").update({"name":"Gname"})
#Delete Data
db.collection("module1").document("485").delete()
#Read After
results = db.collection("module1").get()
for result in results:
    print(result.to_dict())
#Notifications
def on_snapshot(doc_snapshot, changes, read_time):
    for change in changes:
        if change.type.name == 'ADDED':
            print(f"New data: {change.document.to_dict()}")
        elif change.type.name == 'MODIFIED':
            print(f"Modified data: {change.document.to_dict()}")
        elif change.type.name == 'REMOVED':
            print(f"Removed data: {change.document.id}")

doc_ref.on_snapshot(on_snapshot)