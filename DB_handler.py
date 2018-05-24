from Engine_connector import Users
from Engine_connector import Shows
from Engine_connector import db





############# user requests #####################
def create_user(user_json):
    name = user_json["user_info"]["user_name"]
    email = user_json["user_info"]["user_email"]
    password = user_json["user_info"]["user_password"]
    new_user = Users(name, email, password)
    print("user was created")
    db.session.add(new_user)
    db.session.commit()
    print("success!")
    db.session.close()


def delete_user(delete_user_json):
    name = delete_user_json['user_info']['user_name']
    password = delete_user_json['user_info']['user_password']

    Users.query.filter_by(name=name, password=password).delete()
    db.session.commit()
    print("user: " + name +" was deleted")
    db.session.close()


def user_login(login_json):
    user_email = login_json["user_info"]["user_email"]
    user_password = login_json["user_info"]["user_password"]

    exists = db.session.query(Users.password).filter_by(email=user_email).scalar()
    print(exists)
    if(exists!= None):
        if(exists == user_password):
            return True
    return False

def update_user(update_user_json):
    key = update_user_json['update_user']['key']
    old_field = update_user_json['update_user']['old_field']
    new_field = update_user_json['update_user']['new_field']



########### shows requests ########################
def create_show(new_show_json):
    artist_name = new_show_json["show_info"]["artist_name"]
    location = new_show_json["show_info"]["location"]
    date = new_show_json["show_info"]["date"]
    price = new_show_json["show_info"]["price"]

    new_show = Shows(artist_name, location, date, price)
    db.session.add(new_show)
    db.session.commit()
    db.session.close()

