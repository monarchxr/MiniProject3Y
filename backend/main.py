from parser import parse_resume
import json

resume_file = "" #put path of resume file here for now

parsed_data = parse_resume(resume_file)

#save parsed data to json file

with open("output.json", "w", encoding="utf-8") as f:
    json.dump(parsed_data, f, indent=2)

# display parsed results
print("Resume data: ")
for key,value in parsed_data.items():
    print(f"{key.capitalize()}: {value}")