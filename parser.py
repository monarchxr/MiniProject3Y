import pdfplumber
import re
import spacy

nlp = spacy.load("en_core_web_sm")

#function for extracting text from pdf with input path
def extract_text_from_pdf(pdf_path):

    
    text = ""

    with pdfplumber.open(pdf_path) as pdf:

        for page in pdf.pages:

            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"

    
    return text


#function to extract name from text parsed
def extract_name(text):

    """
    Extract name from first line which does not
    contain email or phone number
    """

    lines = text.split("\n")

    for line in lines:
        line = line.strip()

        if line and not re.search(r'@|\d', line):
            return line
        
    
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            return ent.text
        
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