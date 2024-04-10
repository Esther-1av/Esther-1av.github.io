import sqlite3

# Connect to the database #

conn = sqlite3.connect('userInfo.db')
cursor = conn.cursor()

# Create the table #
# this is a very unorginized and unoredered sql database and needs to be cleaned up by someone who understands sql better #

cursor.execute(
    '''CREATE TABLE IF NOT EXISTS email (id INTEGER PRIMARY KEY, email TEXT)'''
)
cursor.execute(
    '''CREATE TABLE IF NOT EXISTS hobbies (id INTEGER PRIMARY KEY, hobbies TEXT)'''
)
cursor.execute(
    '''create table if not exists religion (id integer primary key, religion text)'''
)
cursor.execute(
    '''create table if not exists age (id integer primary key, age text)''')
cursor.execute(
    '''create table if not exists sex (id integer primary key, sex text)''')
cursor.execute(
    '''create table if not exists gender (id integer primary key, gender text)'''
)
cursor.execute(
    '''create table if not exists name (id integer primary key, name text)''')
cursor.execute(
    '''create table if not exists phone (id integer primary key, phone text)''')

# Get the information from the user #

namecorrect = "no"
while namecorrect == "no":
  name = input("What name should we refer to you as: ")
  namecorrect = input("Is this correct (yes, no): " + name + ": ")
  # Insert the users name into the databse #
  cursor.execute("INSERT INTO name (name) VALUES (?)", (name, ))
if namecorrect == "yes":
    email = input("What is your email: ")
    emailcorrect = input("Is this correct (yes, no):"+email+":")
    phone = input("What is your phone number (optional, type n/a if no number is available ): ")
    correctphone = input("Is this correct (yes, no):"+ phone +":")
    while correctphone == "yes":
        age = input("How old are you: ")
        sex = input("What is your sex (male, female, intersex, rather not say, other): ")
        if sex.lower() == "rather not say" or sex.lower() == "other" or sex.lower() == "intersex" or sex.lower() == "male" or sex.lower() == "female":
          pass
        if sex.lower() == "other":
            sex = input("What is your sex: ")
        ethnicity = input(
          "What is your ethnicity (asian, african american, white, multiracial, african, american indian, alaskan native, hawaiian native, hispanic, other, rather not say): ")
        if ethnicity == "other" or ethnicity == "Other":
            ethnicity = (input("what is your ethnicity: "))
            pass
        gender = input(
              "what is your gender identity (man (not specifically trans or cis), women (not specifically trans or cis), transgender, non-binary, agender, genderfluid, genderqueer, other, rather not say): ")
        # Insert the users gender into the databse #
        cursor.execute("INSERT INTO gender (gender) VALUES (?)", (gender,))
        if gender.lower() not in ["man", "woman", "transgender", "non-binary", "agender","genderfluid", "genderqueer", "other", "rather not say"]:
          print(gender)
        else:
          pass
        hobbies = input("What are your Hobbies (separate by ','):")
        religous = input("Are you religious (yes, no): ")
        if religous == "no":
            print("OK")
            print("Thank You")
            break
        if religous == "yes":
            religous = input("What religion do you identify with (christian, buddhist, muslim, jewish, other, rather not say): ")
            print("OK")
            print("Thank You")
            break
        if religous == "other":
            print(input("what religion do you practice:"))
            print("OK")
            print("Thank You")
            break

# Insert the information into the database #

        cursor.execute("INSERT INTO hobbies (hobbies) VALUES (?)", (hobbies,))
        cursor.execute("INSERT INTO religion (religion) VALUES (?)", (religous,))
        cursor.execute("INSERT INTO age (age) VALUES (?)", (age,))
        cursor.execute("INSERT INTO sex (sex) VALUES (?)", (sex,))
        cursor.execute("INSERT INTO gender (gender) VALUES (?)", (gender,))
        cursor.execute("INSERT INTO phone (phone) VALUES (?)", (phone,))
        cursor.execute("INSERT INTO email (email) VALUES (?)", (email, ))
        conn.commit()
