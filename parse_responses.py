import re
import json

def parse_survey_responses(filepath):
    """
    Parses survey response data from a file. This function should only be accessible by authorized personnel.
    """
    people = []
    response_pattern = re.compile(r"Name: (.*), DOB: (.*), Responses: (\[.*\])")

    with open(filepath, 'r') as file:
        for line in file:
            match = response_pattern.match(line.strip())
            if match:
                name, dob, responses_str = match.groups()
                responses = json.loads(responses_str.replace("'", '"'))
                person_data = {
                    'Name': name,
                    'DOB': dob,
                    'Responses': responses
                }
                people.append(person_data)

    return people

def main():
    authorized = input("Enter password for access: ")
    if authorized == "A5":
        people_data = parse_survey_responses('survey_responses.txt')
        for person in people_data:
            print(f"Name: {person['Name']}")
            print(f"Date of Birth: {person['DOB']}")
            print(f"Survey Responses: {person['Responses']}")
            print("-" * 20)
    else:
        print("Unauthorized access.")

if __name__ == "__main__":
    main()