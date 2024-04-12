import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

# Function for email and phone validation

def validate_email(email, characters=['@','.'], min_length=6):
    while True:
        for character in characters:
            if character not in email:
                email = input("Something went wrong, make sure to use only '@' and '.'. Please try again: ")
                break
        if len(email) <= min_length:
            email = input("Your email is not long enough, please try again: ")
        else:
            return email

def validate_phone(phone, characters=['-', '/'], min_length=10):
    while True: 
        for character in characters:
            if character not in phone:
                phone = input("Something went wrong, make sure to only use '-' or '/'. Please try again: ")
                break
        if len(phone) <= min_length or phone.lower() != "n/a":
            phone = input("Your phone number is not long enough, please try again: ")
            break
        correctphone = "no"
        while correctphone.lower() == "no":
            phone = input("What is your phone number: ")
            correctphone = input("Is this correct: {} (yes/no)".format(phone))
            if correctphone.lower() == "yes":
                break
        else: 
            return phone

# SQLite database connection and user info storage

@app.route('/', methods=['GET', 'POST'])
def index():
    conn = sqlite3.connect('user_info.db')
    c = conn.cursor()

    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        email = validate_email(request.form['email'])
        phone = validate_phone(request.form['phone'])

        c.execute("INSERT INTO users (name, age, email, phone) VALUES (?, ?, ?, ?)", (name, age, email, phone))
        conn.commit()

        return "Information added successfully for '{}'".format(email)

    return render_template('index.html')

if __name__ == '__main__':
    app.run()
