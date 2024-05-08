# COVID_Diagnosis_Wizard
INST326 Final Project

# Final.py
This is our main script. "python3 Final.py" or "python Final.py" in the command
line runs the script. Upon running, it will prompt the user for inputs. After 
inputting responses for each prompt, a short message is returned indicating the
responses are saved and a condition check was successful. Saving responses
generates a text file in the working directory titled "survey_responses.txt."

# parse_responses
This script compliments our main script. Runs using "python3 parse_responses.py"
or "python parse_responses.py" in the command line. Upon running, it will ask the
user for a password. If the incorrect password is entered, a message is returned
indicating its error and that access to "survey_responses.txt" is denied. If the
correct password is entered, it will return an organized version of what is stored
in "survey_responses.txt." The password is "A5."

# Attribution
**Method/Function** | **Primary Author** | **Techniques Demonstrated**
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
get_responses       |      Kevin Chan    |  List Comprehension
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -
survey              |      Allen Jiang   |  with Statement, f-strings
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
parse_responses.py  |      Anh Dang      |  Regular Expressions
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
Person              |      Seulgi Hong   |  Classes
- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 
covid_graph         |      Khai Ta       |  pyplot
