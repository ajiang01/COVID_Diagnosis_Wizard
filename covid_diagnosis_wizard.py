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
            
            
            
            
            