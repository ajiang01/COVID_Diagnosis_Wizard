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
            
            
            
            
            