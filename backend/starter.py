from backend.parser import parse_resume
import json

def process_resume(resume_file_path):


    parsed_data = parse_resume(resume_file_path)

    #save parsed data to json file

    with open("output.json", "w", encoding="utf-8") as f:
        json.dump(parsed_data, f, indent=2)

    # display parsed results
    print("Resume data: ")
    
    for key,value in parsed_data.items():
        print(f"{key.capitalize()}: {value}")