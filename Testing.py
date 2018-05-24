import json

import DB_handler

user2 = '''{"user_info": {"user_name": "tom", "user_email": "tom@gmail.com", "user_password": "11111"}}'''
user = '''{"user_info": {"user_name": "ido", "user_email": "ido@gmail.com", "user_password": "00000"}}'''
user3 = '''{"user_info": {"user_name": "gadi", "user_email": "gadi@gmail.com", "user_password": "44421"}}'''
user4 = '''{"user_info": {"user_name": "ido", "user_email": "ido@gmail.com", "user_password": "1212"}}'''

# show = '''{"show_info": {"artist_name": "static & benEl", "location": "zapa tel-aviv", "date": "25.6.2018","price":"350"}}'''
show2 = '''{"show_info": {"artist_name": "omer adam", "location": "beer-sheva", "date": "20180518","price":"450"}}'''
show3 = '''{"show_info": {"artist_name": "mosh-ben-ari", "location": "eilat", "date": "20180614","price":"150"}}'''

# userToDelete = '''{"delete_info": {"user_name": "tom","user_password": "11111"}}'''
# userToDelete_json = json.loads(userToDelete)
# user_4 = json.loads(user4)
# DB_handler.create_user(user_4)
login_ido = '''{"user_info": {"user_email": "ido@gmail.com", "user_password": "11111"}}'''
login_json = json.loads(login_ido)

result = DB_handler.user_login(login_json)
print(result)

