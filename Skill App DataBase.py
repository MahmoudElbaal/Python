##############################
##### Skill App Database #####
##############################
# Import SQLite Module
import sqlite3

# Create DataBase And Connect
db = sqlite3.connect("app.db")
db.execute('''CREATE TABLE IF NOT EXISTS skills (name TEXT , progress INTEGER , user_id INTEGER)''')
# Setting Up The Cursor
cr = db.cursor()


def commit_and_close():
  """ Commit Changes and Close Connection To Database """
  db.commit()    # Save (Commit) Changes
  db.close()     # Close DataBase
  print("Connection To DataBase Is Closed ")

# My User ID
uid = 1

# Input Big Massage
input_message = """
What Do You Want To Do ?
"s" => Show All Skills
"a" => Add New Skill
"d" => Delete A Skill
"u" => Update Skill Progress
"q" => Quit The App
Choose Option :
"""

# Input Option
user_input = input(input_message).strip().lower()

# Command List
commands_list = ["s", "a", "d", "u", "q"]

# Define The Methods
def show_skills():
 cr.execute(f"SELECT * from skills Where user_id = {uid}")
 results = cr.fetchall()
 print(f"You Have {len(results)} Skills")
 if len(results) > 0:
  print("Showing Skills With Progress:")
 for row in results:
   print(f"Skill => {row[0]}", end=" ")
   print(f"Progress => {row[1]}%")
 commit_and_close()

def add_skill():
 skill = input("Write Skill Name: ").strip().capitalize()
 cr.execute(f"SELECT name from skills Where name = '{skill}' and user_id = '{uid}'")
 results = cr.fetchone()
 if results == None:  # There Is No Skill With The Same Name In db
   Progress = input("Write Skill Progress: ").strip()
   cr.execute(f"insert into skills(name, Progress, user_id) values('{skill}', '{Progress}' , '{uid}')")
 else:                # There Is A Skill With The Same Name In db
  print("This Skill Already Exits , You Cannot Add The Same Skill Twice")
  
  new_update = input("Would You Like To Update The Progress of This Skill 'Y' or 'N': ").strip().lower()
  if new_update == 'y':
   Progress = input("Write The New Skill Progress: ").strip()
   cr.execute(f"UPDATE skills set progress ='{Progress}' where name ='{skill}' and user_id ='{uid}'")
  else : new_update == 'n'
   
 commit_and_close()

  


def delete_skill():
 skill = input("Write Skill Name: ").strip().capitalize()
 cr.execute(f"DELETE from skills where name ='{skill}' and user_id ='{uid}'")
 commit_and_close()

def update_skill():
 skill = input("Write Skill Name: ").strip().capitalize()
 Progress = input("Write The New Skill Progress: ").strip()
 cr.execute(f"UPDATE skills set progress ='{Progress}' where name ='{skill}' and user_id ='{uid}'")
 commit_and_close()  

# Check If Command Exits
if user_input in commands_list :
#  print(f"Your Command Is:{user_input}")
 if user_input == "s":
   show_skills()
 elif user_input == "a": 
   add_skill()
 elif user_input == "d":
   delete_skill() 
 elif user_input == "u":
   update_skill()
 else:
   print("App Is Closed.")
   commit_and_close()
else:
  print(f"Sorry This Command \"{user_input}\" Is not Found")

