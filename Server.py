from flask import Flask, render_template, request, redirect, url_for, flash
import DB_handler
from Engine_connector import app
import json



# app = Flask(__name__)
print("__name__ is ", __name__)



# main page
@app.route('/',methods=['GET', 'POST'])
def index():
    error = ''
    try:
        if request.method == "POST":
            data = request.get_json()
            print(data)
            if not request.is_json:
                print("json was not found")
                return "<h2>Problem with the Json</h2>"
            print(DB_handler.user_login(data))
            if DB_handler.user_login(data):
                print("successfuly logged in")
                return json.dumps(data)

    except Exception as e:
        print("exception")
    return render_template('main.html', error=error)




# Route for handling the login page logic
@app.route('/register', methods=['GET', 'POST'])
def register():
    error = ''
    try:
        if request.method == "POST":
            data = request.get_json()
            print(data)
            if not request.is_json:
                print("json was not found")
                return "<h2>Problem with the Json</h2>"
            result = DB_handler.create_user(data)
            print(result)
            # test
            return json.dumps(result)

    except Exception as e:
         print("exception")
    return render_template('Form.html', error=error)

# Route for handling the login page logic
@app.route('/delete', methods=['GET', 'POST'])
def delete():
    error = ''
    try:
        if request.method == "POST":
            data = request.get_json()
            print(data)
            if not request.is_json:
                print("json was not found")
                return "<h2>Problem with the Json</h2>"
            DB_handler.delete_user(data)
            print("account was deleted")
            return json.dumps(data)

    except Exception as e:
         print("exception")
    return render_template('Delete_User.html', error=error)


# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    error = ''
    try:
        if request.method == "POST":
            data = request.get_json()
            print(data)
            if not request.is_json:
                print("json was not found")
                return "<h2>Problem with the Json</h2>"
            DB_handler.user_login(data)
            print("finish db update")
            return json.dumps(data)

    except Exception as e:
         print("exception")
    return render_template('index.html', error=error)

@app.route('/loginFinished')
def loginFinished():
        return "<h2>Thank you for login!</h2>"


@app.route('/profile/<username>')
def profile(username):
    return render_template("profile.html", username=username)

if __name__ == '__main__':
    app.run(debug=True)


