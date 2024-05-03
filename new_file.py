import matplotlib.pyplot as plt
import re
from datetime import datetime

def get_response(user_symptoms):
    """
    Analyzes user's responses to determine the likelihood of having COVID-19.
    """
    yes_count = sum(1 for response in user_symptoms if response.lower() == 'yes')

    if yes_count >= 3:
        response = "You seem to likely have COVID-19."
    elif yes_count == 1 or yes_count == 2:
        response = "There's a possibility you might have COVID-19. Take precautions and consider getting tested ASAP!!!"
    else:
        response = "You most likely don't have COVID-19."

    print(f"Based on your responses, {response}")

def survey():
    """
    Conducts an interactive survey asking the user about symptoms related to COVID-19.
    """
    responses = []

    print("Please answer the following questions with 'Yes' or 'No'.")
    name = input("Enter your name: ")
    dob = input("Enter your date of birth. Use mm/dd/yy format: ")
    cough = input("(Yes/No) Exhibiting persistent coughing: ")
    responses.append(cough)
    fever = input("(Yes/No) Exhibiting fever: ")
    responses.append(fever)
    nausea = input("(Yes/No) Exhibiting nausea: ")
    responses.append(nausea)
    sore_throat = input("(Yes/No) Exhibiting sore throat: ")
    responses.append(sore_throat)
    
    get_response(responses)

def covid_graph(symptom_counts):
    """
    Plots a bar graph of potential COVID-19 cases based on symptom frequencies.
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

def age_group_graph(person):
    """
    Plots a bar graph showing COVID-19 cases by age group.
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
        """
        return self.symptoms

    def get_age(self):
        """
        Calculates and returns the person's age based on their birthdate.
        """
        birth_date = datetime.strptime(self.birthdate, "%m/%d/%y")
        today = datetime.now()
        return (today.year - birth_date.year) - ((today.month, today.day) < (birth_date.month, birth_date.day))

    @classmethod
    def store_people_sorted_lastname(cls):
        """
        Returns a list of people sorted by their last name.
        """
        return sorted(cls.people, key=lambda person: person.name.split()[-1])

    @classmethod
    def display_customers(cls):
        """
        Prints a formatted string of all customers' data.
        """
        for customer, data in cls.customers.items():
            print(f"{customer}: {data}")

def parse_data(filepath):
    """
    Parses data from a file to create Person objects for each recorded individual.
    """
    people = []
    person_data = {}
    with open(filepath, 'r') as file:
        for line in file:
            if line.strip() == "":
                if person_data:
                    name = person_data['Name']
                    birthdate = person_data['Birthdate']
                    symptoms = person_data['Symptoms'].split(', ')
                    symptoms = [sym.split(': ')[1] for sym in symptoms]
                    report_date = person_data['Date']
                    people.append(Person(name, birthdate, symptoms, report_date))
                    person_data = {}
            else:
                key, value = line.strip().split(': ', 1)
                person_data[key] = value

        if person_data:
            name = person_data['Name']
            birthdate = person_data['Birthdate']
            symptoms = person_data['Symptoms'].plit(', ')
            symptoms = [sym.split(': ')[1] for sym in symptoms]
            report_date = person_data['Date']
            people.append(Person(name, birthdate, symptoms, report_date))

    return people

def main():
    survey()

if __name__ == "__main__":
    main()
