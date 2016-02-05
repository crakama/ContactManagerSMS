""'
Thisis aPython console application that enables a users to manage thier contacts. 
It supports creating, retrieving, and searching phonebook entries consisting of a name and a phone number.
Stores the entries in SQLite database and allows sending of a text message to specific mobile number

Initial Requirements specification: The system should have enabled the user to:

•	add a person to contacts list with the following command: add -n <name> -p <phone number>
•	save this contact in an SQLite database
•	to search for a person’s contact by issuing a command: search “Andela” should print the Andela’s phone number. 
•	In case we have more than one person using the name Andela, it should ask:Which Andela? [1] James [2] Hellen [3] Joshua i.e. James Andela, Hellen Andela, etc.
•	The system should be able to send simple one-way texts to the people in the contacts. e.g. a command text James -m “We meet at Hogwarts, 3 PM, Anthony” / Use any appropriate SMS Gateway API e.g. Twilio, AfricasTalking, etc.

What it does:
•	adds a person to contacts list with the following command: add <name> <phone number>
•	saves this contact in an SQLite database
•	searches for a person’s contact by issuing a command: search “Andela” should print the Andela’s phone number. 
•	Sends simple one-way texts to the people in the contacts. e.g. a command text James -m “We meet at Hogwarts, 3 PM, Anthony”  using AfricasTalking SMS Gateway API

What it does not do:

•	In case we have more than one person using the name Andela, it should ask:Which Andela? [1] James [2] Hellen [3] Joshua i.e. James Andela, Hellen Andela, etc.
•   run as one executible file (you have to run main_file.py as a normal python sript at the console for search and add functionalies. 
    Then run sms.py for sending message)
•  Retrieve contacts directly from the database, it uses contacts defined manually in a list within the code

Requirements for running the scripts:

To run the program on a terminal:
 
•	Create your project/working directory on your local drive
•	Install python compiler 2.7.11 on your system and add its path to the environment variables.
•	Install virtual environment in your project working directory.
•	Execute the script by issuing the following commands:
    o	To add contact:>>> main_file.py add <name> <mobile number>
    o	To Search contact >>> main_file.py lookup <name> 
    o	To Send message >>> sms.py  (press enter)

• Install SQLite browser if you want to verify that the contacts are biend added to the database. 
While on the SQlite database browser got to >> open database, navigate to your project folder where you have been running your main_file.py and import the database

"""