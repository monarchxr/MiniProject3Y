# resume analysis and job recommendation

## purpose
Analyze resumes to identify missing skills, either for:
- A specific job role (user provides this)
- general software developer competency

## core features
- pdf resume upload and parsing
- skill extraction from resume text
- AI powered gap analysis using Groq
- Structured skill recommendations

## tech stack
- frontend: vanilla html/css/js
- backend: python+flask
- pdf processing: pdfplumber
- AI analysis - Groq API
- Deployment - local

# constraints
- pdf only
- max file size 10mb
- single user?
- temp file storage