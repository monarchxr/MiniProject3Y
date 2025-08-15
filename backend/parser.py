import pdfplumber
import re
import spacy

nlp = spacy.load("en_core_web_sm")

#function for extracting text from pdf with input path
def extract_text_from_pdf(pdf_path):
    text = ""

    try:
        with pdfplumber.open(pdf_path) as pdf:
            pages = pdf.pages
            for page in pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
                else:
                    text += "\n"
    except Exception as e:
        print(f"Error occurred while extracting text from PDF: {e}")

    return text



#function to extract name from text parsed
def extract_name(text):
    # first lets get all lines from the text

    lines = text.split("\n")

    # usually the name is in the first 1-5 lines
    # so we'll look for a line w/o email or phone

    for line in lines:
        line = line.strip()
        if line and not re.search(r'@|\d', line):
            return line
        
    # if we dont find it,
    # we'll use NER (named entity recognition) using spacy

    doc = nlp(text)

    # traverse the entities until you find one matching with PERSON

    for ent in doc.ents:
        if ent.label_ == "PERSON":
            return ent.text
        
    # if nothing found
    return None


#function to extract email for parsed text
def extract_email(text):
    mail = re.search(r"[\w\.-]+@[\w\.-]+\.\w+", text)
    
    if mail:
        return mail.group(0)
    
    return None


#function to extract skills
def extract_skills(text):

    doc = nlp(text)
    skills = []
    
    pattern = r"(proficient in|experienced with|skilled in|knowledge of)\s+([a-zA-Z0-9.,\s]+)"
    matches = re.findall(pattern, text.lower())
    
    for match in matches:
        for skill in match[1].split(","):
            skills.add(skill.strip().capitalize())
    
    skill_labels = ["ORG", "PRODUCT", "SKILL", "WORK_OF_ART"]

    for ent in doc.ents:
        if ent.label_ in skill_labels:
            skills.add(ent.text.strip())

    return list(set(skills))


#function for parsing
def parse_resume(path):
    text = extract_text_from_pdf(path)

    return{
        "name": extract_name(text),
        "email": extract_email(text),
        "skills": extract_skills(text)
    }