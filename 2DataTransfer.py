
import sys
import subprocess
import csv
import google.cloud
import firebase_admin
import requests
import os
from firebase_admin import credentials, firestore    



print(f'Kullanıcı: {os.getlogin()}')
print("Internet bağlantısı:", end =" ")
connection = None
try:
    r = requests.get("https://google.com")
    r.raise_for_status()
    connection = True
except:
    connection = False
finally:
    if connection==True:
        print("Var.")
    else:
        print("Yok.")
    print("-"*60)  

cred = credentials.Certificate("serviceAccountKey.json")
app = firebase_admin.initialize_app(cred)

store = firestore.client()

file_path = "./amp.csv"
collection_name = "products"



secim="0"

print("1. Veriyi göster")
print("2. Firebase e aktar")
print("3. Firebase i kontrol et")
print("4. Çıkış")

secim = input("Tercihiniz (1,2,3,4) > ")

print("-"*60)

if secim=="1":
    docs = store.collection(u'products').stream()
    records=0
    for doc in docs:
        print(f'{doc.id} => {doc.to_dict()}')
        records+=1
    print("Gösterilen kayıt sayısı: ",records)
    
if secim=="4":
    print("Bitti")

if secim=="2":
    
    def batch_data(iterable, n=1):
        l = len(iterable)
        for ndx in range(0, l, n):
            yield iterable[ndx:min(ndx + n, l)]

    data = []
    headers = []
    with open(file_path) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                for header in row:
                    headers.append(header)
                line_count += 1
            else:
                obj = {}
                for idx, item in enumerate(row):
                    obj[headers[idx]] = item
                data.append(obj)
                line_count += 1
        print("-"*60) 
        print(f'{line_count} kayit işlendi.')

    for batched_data in batch_data(data, 499):
        batch = store.batch()
        for data_item in batched_data:
            doc_ref = store.collection(collection_name).document()
            batch.set(doc_ref, data_item)
        batch.commit()
    sys.exit()

if secim=="3":
    data = []

    docs = store.collection(u'products').get()
    for doc in docs:
        data.append(doc.to_dict())  
    print(len(data),"Kayıt var.")
    


print("-"*60)       
print("Bitti")
