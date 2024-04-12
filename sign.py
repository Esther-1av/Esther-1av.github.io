import sqlite3

# validate email addresses

def validate_email(email_address, characters=['@','.'], min_length=6):
    while True:
        for character in characters:
            if character not in email_address:
                email_address = input("Something went wrong, please try again: ")
                break
        if len(email_address) <= min_length:
            email_address = input("Your email is not long enough, please try again: ")
        else:
            return email_address

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
