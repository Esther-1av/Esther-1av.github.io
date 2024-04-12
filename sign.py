import sqlite3

# validate email 

def validate_email(email, characters=['@','.'], min_length=6):
    while True:
        for character in characters:
            if character not in email:
                email = input("Something went wrong, make sure to only use '@', and '.'. Please try again: ")
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
        if len(phone) <= min_length or phone.lower() != n/a:
            phone = input("Your Phone number is not long enough, please try again")
            break
        else: 
            return phone

try:

    # Connect to database
  
    conn = sqlite3.connect('user_info.db')
    c = conn.cursor()

    # Create a table to store user information
  
    c.execute('''CREATE TABLE IF NOT EXISTS users (name TEXT, age INTEGER, email TEXT)''')

    # Validate and store user information
  
    name = input("What should we call you: ")
    age = int(input("How old are you: "))
    email = validate_email(input("What is your email: "))
    phone = input("What is your phone number (optional, type n/a if no number is available ): ")

    # Insert validated user information into the database
  
    c.execute("INSERT INTO users (email, name, age) VALUES (?, ?, ?)", (email, name, age))
    conn.commit()
    print("")
    print("Information added for '{}'".format(email))

    # Retrieve all information from the table
  
    c.execute("SELECT * FROM users")
    rows = c.fetchall()

    # Display information in database
    
    for row in rows:
      name, age, email = row[:3]
      print("")
      print("Email: {}, Name: {}, Age: {}".format(email, name, age))

except sqlite3.Error as e:
    print("An error occurred:", str(e))

finally:
  
    # Close database connection
  
    conn.close()
