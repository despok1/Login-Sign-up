from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
uri = "mongodb+srv://telebot:198219821@cluster0.t0qiw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri, server_api=ServerApi('1'))
db = client["login-sign-up"]
users_collection = db["users"]

full_name = "damir1"
email = "damir@gmail.com1"
password = "damir1231"

def save_user_db(full_name,email,password):
    users_collection.insert_one({
        "full_name" : full_name,
        "email" : email,
        "password" : password,
        })


def check_user_in_db(email):
    result = users_collection.find_one({ "email" : email })
    print(result)
    if result: return True
    else: return False
    
check = check_user_in_db(email)  
if check == False:  
    save_user_db(full_name,email,password)
    
