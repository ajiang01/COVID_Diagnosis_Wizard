import matplotlib.pyplot as plt
import re
from datetime import datetime



def get_response(symptoms_file, user_symptoms):
    """
    Args:
        symptoms_file (str): The path to the file that contains the symptoms 
        and their responses.
        
        user_symptoms (list): The list of symptoms reported by the user.

    Returns:
        str: A message that indicates the likelihood of the user having 
        COVID-19 based on their symptoms.
    """
    with open(symptoms_file, 'r') as file:
        symptoms_dict = {}
        for line in file:
            symptom, response = line.strip().split(':')
            symptoms_dict[symptom.strip()] = response.strip()

    yes_count = sum(1 for symptom in user_symptoms if symptom.lower() == 'yes')

    if yes_count >= 2:
        response = "You seem to likely have COVID-19."
    elif yes_count == 1:
        response = "There's a possibility you might have COVID-19. Take \
            precautions and cconsider getting tested ASAP!!!"
    else:
        response = "You most likely don't have COVID-19."

    print(f"Based on your responses, {response}")

def survey():
    """
    Asks for user input a series of questions 3 times to simulate an online survey
    related to COVID.
    
    Side effects:
        Creates text file containing user's inputs by line
    """
    with open("survey_responses.txt", "w", encoding = "utf-8") as file:
            name = input("Enter your name: ")
            file.write(f"{name}\n")
            
            dob = input("Enter your date of birth. Use mm/dd/yy format: ")
            file.write(f"{dob}\n")
            
            cough = input("(Yes/No) Exhibiting persistent coughing: ")
            file.write(f"{cough}\n")
            
            fever = input("(Yes/No) Exhibiting fever: ")
            file.write(f"{fever}\n")
            
            nausea = input("(Yes/No) Exhibiting nausea: ")
            file.write(f"{nausea}\n")
            
            sore_throat = input("(Yes/No) Exhibiting sore throat: ")
            file.write(f"{sore_throat}\n")

def covid_graph(symptom_counts):
    """Makes a graph of potential covid cases based symptoms

    Args:
        symptom_counts (dictionary): A dictonary of the symptoms
        that are present and how often they occured. 
    """
    symptom_names = list(symptom_counts.keys())
    symptom_values = list(symptom_counts.values())

    plt.figure(figsize=(10, 6))
    plt.bar(symptom_names, symptom_values, color="skyblue")
    plt.title("Number of Potential COVID Cases")
    plt.xlabel("Symptoms")
    plt.ylabel("Number of Cases")
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()

def agre_group_graph(person):
    """Sees which group has the most covid cases 

    Args:
        person (person): the user of the program 
    """
    age_groups = {
        "0-19": 0,
        "20-39": 0,
        "40-59": 0,
        "60-79": 0,
        "80+": 0
    }

    for user in person:
        age = user.get_age()
        if age is not None:
            if age <= 19:
                age_groups["0-19"] += 1
            elif age <= 39:
                age_groups["20-39"] += 1
            elif age <= 59:
                age_groups["40-59"] += 1
            elif age <= 79:
                age_groups["60-79"] += 1
            else:
                age_groups["80+"] += 1
    
    age_groups_names = list(age_groups.keys())
    age_groups_values = list(age_groups.values())

    plt.figure(figsize=(10, 6))
    plt.bar(age_groups_names, age_groups_values, color="yellow")
    plt.title("Age Groups and COVID Cases")
    plt.xlabel("Age Groups")
    plt.ylabel("Number of Cases")
    plt.tight_layout()
    plt.show()    
    
class Person:
    """
    Represents a person with details relevant to COVID-19 symptom tracking.

    Attributes:
        name (str): The full name of the person.
        birthdate (str): The birthdate of the person formatted as "mm/dd/yy".
        symptoms (list of str): A list of symptoms with responses ('Yes' or 'No').
        report_date (str): The date when the symptoms were reported, formatted as "mm/dd/yy".

    Methods:
        get_symptoms: Returns a list of the person's symptoms.
        get_age: Calculates and returns the person's age based on their birthdate.
    """
    people = []
    customers = {}
    
    def __init__(self, name, birthdate, symptoms, report_date):
        self.name = name
        self.birthdate = birthdate
        self.symptoms = symptoms
        self.report_date = report_date
        Person.people.append(self)
        Person.customers[name] = {
            'Name': name,
            'Birthdate': birthdate,
            'Symptoms': symptoms,
            'Report Date': report_date
        }

    def store_people_sorted_lastname(cls):
        """
        Class method to return the people sorted alphabetically by last name.

        Returns:
            list of Person: People sorted by last name.
        """
        
        return sorted(cls.people, key = lambda person: person.name.split()[-1])
    
    def display_customers(cls):
        """
        Class method to display all customers' data stored in the class 
        attribute `customers`.
        
        Returns:
            prints each customer's name followed by their corresponding data in 
            a formatted string.
        """
        for customer, data in cls.customers.items():
            print(f"{customer}: {data}")

def parse_data(filepath):
    # Regular expressions for each piece of data
    pattern = re.compile(r"^(Name|Birthdate|Symptoms|Date): (.+)$")
    
    people = []
    person_data = {}

    with open(filepath, 'r') as file:
        for line in file:
            line = line.strip()
            if line == "":
                if person_data:
                    # When a complete person's data has been gathered, process it
                    people.append(create_person_from_data(person_data))
                    person_data = {}
            else:
                match = pattern.match(line)
                if match:
                    key, value = match.groups()
                    if key == 'Symptoms':
                        # Process symptoms into a dictionary if required by other parts of the code
                        symptoms = dict(sym.split(': ') for sym in value.split(', '))
                        person_data[key] = symptoms
                    else:
                        person_data[key] = value
        if person_data:
            people.append(create_person_from_data(person_data))
            
    return people

def create_person_from_data(data):
    # Assuming the person is expected to be a dictionary or similar object
    return data

def main():
    survey()
    
if __name__ == "__main__":
    main()