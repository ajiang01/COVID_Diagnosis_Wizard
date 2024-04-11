import matplotlib.pyplot as plt

def get_response(symptoms_file, user_symptoms):
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
    with open("survey_responses.txt", "w", encoding = "utf-8") as file:
        for responses in range (1):
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

def count_symptoms(users):
    symptom_counts = {}
    for user in users:
        symptoms = user.get_symptoms()
        for symptom, value in symptoms.items():
            if value == 'yes':
                symptom_counts[symptom] = symptom_counts.get(symptom, 0) + 1
    return symptom_counts

def covid_graph(symptom_counts):

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

def age_groups(users):
    age_groups = {
        "0-19": 0,
        "20-39": 0,
        "40-59": 0,
        "60-79": 0,
        "80+": 0
    }

    for user in users:
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

    return age_groups
            
def age_groups_graph(age_groups):

    age_groups_names = list(age_groups.keys())
    age_groups_values = list(age_groups.values())

    plt.figure(figsize=(10, 6))
    plt.bar(age_groups_names, age_groups_values, color="yellow")
    plt.title("Age Groups and COVID Cases")
    plt.xlabel("Age Groups")
    plt.ylabel("Number of Cases")
    plt.tight_layout()
    plt.show()    