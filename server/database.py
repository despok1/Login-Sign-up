from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import hashlib


class Database:
    # конструктор хранитель глобальних перемених
    def __init__(self,user_email:str,password:str,full_name:str):
        self.uri = "mongodb+srv://telebot:198219821@cluster0.t0qiw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
        self.client = MongoClient(self.uri, server_api=ServerApi('1'))
        self.db = self.client["login-sign-up"]
        self.users_collection = self.db["users"]

        self.full_name = full_name
        self.email = user_email
        self.password = password
        self.result = None
        
    # Шифруем пароли 
    def encrypt(self):    
        self.hash_sha512 = hashlib.sha512(self.password.encode()).hexdigest()    
        
    # Сохроняем юзера в базу даних
    def save_user_db(self):
        self.encrypt()
        self.users_collection.insert_one({
            "full_name" : self.full_name,
            "email" : self.email,
            "password" : self.hash_sha512,
            })

    # проверка юзера в базе даних
    def check_user_in_db(self):
        self.result = self.users_collection.find_one({ "email" : self.email })
        if self.result: return False
        else: return True
        
    # проверка даних юзера (login) 
    def check_user_for_login(self,user_email:str,password:str):
        user_obj = self.users_collection.find_one({ "email" : user_email })
        isUserLogined = False

        if user_obj:
            user_hash = user_obj.get("password")
            if user_hash == hashlib.sha512(password.encode()).hexdigest():
                isUserLogined = True

        return isUserLogined
    
    # регистрация
    def registration(self):
        check = self.check_user_in_db()  

        if check == True:  
            self.save_user_db()
            
        return check

