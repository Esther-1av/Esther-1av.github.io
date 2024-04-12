import sqlite3
 
# Connect to the database #

conn = sqlite3.connect('userInfo.db')
cursor = conn.cursor()

# Create the table #
# this is a very unorginized and unoredered sql database and needs to be cleaned up by someone who understands sql better #


cursor.execute(
  '''create table if not exists name (id INTEGER PRIMARY KEY, name TEXT)''')
cursor.execute(
    '''CREATE TABLE IF NOT EXISTS email (id INTEGER PRIMARY KEY, email TEXT)''')
cursor.execute(
  '''create table if not exists phone (id INTEGER PRIMARY KEY, phone INTEGER)''')
cursor.execute(
  '''create table if not exists age (id INTEGER PRIMARY KEY, age INTEGER)''')
cursor.execute(
  '''create table if not exists ethnicity (id INTEGER PRIMARY KEY, ethnicity TEXT)''')
cursor.execute(
    '''create table if not exists gender (id INTEGER PRIMARY KEY, gender TEXT)''')
cursor.execute(
  '''create table if not exists sex (id INTEGER PRIMARY KEY, sex TEXT)''')
cursor.execute(
    '''CREATE TABLE IF NOT EXISTS sexuality (id INTEGER PRIMARY KEY, sexuality TEXT)''')
cursor.execute(
    '''CREATE TABLE IF NOT EXISTS hobbies (id INTEGER PRIMARY KEY, hobbies TEXT)''')
cursor.execute(
    '''create table if not exists religion (id INTEGER PRIMARY KEY, religion TEXT)''')


# Get the information from the user #

namecorrect = "no"
terminate = "false"
while namecorrect == "no":
  name = input("What name should we refer to you as: ")
  namecorrect = input("Is this correct (yes, no): " + name + ": ")
  # Insert the users name into the databse #
  cursor.execute("INSERT INTO name (name) VALUES (?)", (name, ))
if namecorrect == "yes":
    email = input("What is your email: ")
    emailcorrect = input("Is this correct (yes, no):"+email+":")
    while emailcorrect == "no":
      email = input("What is your email: ")
      emailcorrect = input("Is this correct (yes, no):" + email + ":")
    while emailcorrect == "yes" and terminate == "false":
      phone = input("What is your phone number (optional, type n/a if no number is available ): ")
      correctphone = input("Is this correct (yes, no):"+ phone +":")
      while correctphone == "no":
        phone = input("What is your phone number *optional* ( type n/a if no number is available ): ")
        correctphone = input("Is this correct (yes, no):"+ phone +":")
      while correctphone == "yes" and terminate == "false":
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
        while gender.lower() == "other":
            gender = input("what is your gender identity: ")
        # Insert the users gender into the databse #
            cursor.execute("INSERT INTO gender (gender) VALUES (?)", (gender,))
        sexuality = input ("what is your sexuality (straight, gay, lesbian, bisexual, pansexual, aspec (asexual spectrum), arospec (aromantic spectrum), queer, questioning,  other, rather not say :")
        while sexuality.lower() == "other":
            sexuality = input("what is your sexuality: ")
        hobbies = input("What are your Hobbies (separate by ','):")
        religous = input("Are you religious (yes, no): ")
        if religous == "no":
            print("OK")
            print("Thank You")
            terminate = "true"
        if religous == "yes":
            religous = input("What religion do you identify with (christian, buddhist, muslim, jewish, other, rather not say): ")
            print("OK")
            print("Thank You")
            terminate = "true"
        if religous == "other":
            print(input("what religion do you practice:"))
            print("OK")
            print("Thank You")
            terminate = "true"
      
# Insert the information into the database #

        cursor.execute("INSERT INTO hobbies (hobbies) VALUES (?)", (hobbies,))
        cursor.execute(
          "INSERT INTO sexuality (sexuality) VALUES (?)", (sexuality,))
        cursor.execute("INSERT INTO ethnicity (ethnicity) VALUES (?)", (ethnicity,))
        cursor.execute("INSERT INTO religion (religion) VALUES (?)", (religous,))
        cursor.execute("INSERT INTO age (age) VALUES (?)", (age,))
        cursor.execute("INSERT INTO sex (sex) VALUES (?)", (sex,))
        cursor.execute("INSERT INTO gender (gender) VALUES (?)", (gender,))
        cursor.execute("INSERT INTO phone (phone) VALUES (?)", (phone,))
        cursor.execute("INSERT INTO email (email) VALUES (?)", (email, ))
        conn.commit()
