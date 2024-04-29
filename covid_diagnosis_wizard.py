import matplotlib.pyplot as plt
import re


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
        for responses in range (3):
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
            
    survey()

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

    def get_symptoms(self):
        """
        Returns the list of symptoms the person has reported.

        Returns:
            list of str: Symptoms reported by the person.
        """
        return self.symptoms

    def get_age(self):
        """
        Calculates the person's current age based on their birthdate.

        Returns:
            int: Age of the person.
        """
        from datetime import datetime
        birth_date = datetime.strptime(self.birthdate, "%m/%d/%y")
        today = datetime.now()
        return (today.year - birth_date.year) - ((today.month, today.day) < (birth_date.month, birth_date.day))
    
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
    """
    Parses a text file containing people's data formatted in specific blocks separated by lines.

    Each block contains details of a person (name, birthdate, symptoms, report date) separated by ': '. 
    The symptoms are listed with their respective responses ('Yes' or 'No') and must be processed to store only the responses.

    Args:
        filepath (str): The path to the file containing structured data blocks.

    Returns:
        list of Person: A list of Person objects created from the data in the file.

    """
    people = []
    person_data = {}
    with open(filepath, 'r') as file:
        for line in file:
            if line.strip() == "":  # Use an empty line as a separator between entries
                if person_data:
                    # Process the collected data block
                    name = person_data['Name']
                    birthdate = person_data['Birthdate']
                    symptoms = person_data['Symptoms'].split(', ')  # Adjust based on actual symptom format
                    symptoms = [sym.split(': ')[1] for sym in symptoms]  # Extract 'Yes' or 'No'
                    report_date = person_data['Date']
                    people.append(Person(name, birthdate, symptoms, report_date))
                    person_data = {}  # Reset for next block
            else:
                key, value = line.strip().split(': ', 1)
                person_data[key] = value

        # Handle the last block if the file doesn't end with a blank line
        if person_data:
            name = person_data['Name']
            birthdate = person_data['Birthdate']
            symptoms = person_data['Symptoms'].split(', ')
            symptoms = [sym.split(': ')[1] for sym in symptoms]
            report_date = person_data['Date']
            people.append(Person(name, birthdate, symptoms, report_date))

    return people
