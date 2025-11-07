[User browser]
        |
        |   (Upload pdf + optional job desc)
        v
[Frontend (index.html)]
        |
        |   (post)
        v
[Flask backend]
        |
        |   (validate and save temporarily)
        v
[pdfplumber extraction]
        |
        |   (extract text)
        v
[skill extraction]
        |
        |   (extract skills)
        v
[Groq API]
        |
        |   analyze gaps (different prompt based on job desc)
        v
[response send]
        |
        |   return json to frontend
        v
[display result]