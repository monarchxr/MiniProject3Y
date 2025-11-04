from flask import Flask, request, render_template
import os
from backend.parser import parse_resume

app = Flask(__name__, template_folder="frontend")

# @app.route("/", methods=['GET'])
# def index():
#     return render_template("index.html")


upload_folder = "backend/uploads"
os.makedirs(upload_folder, exist_ok=True)

resume_path = ""

@app.route("/", methods=['GET','POST'])
def receive_resume():
    if request.method == 'POST':

        resume = request.files["resume"]

        res_path = os.path.join(upload_folder, resume.filename)
        resume.save(res_path)
        parse_resume(res_path)

        return "Resume uploaded successfully"
    
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
    # parse_resume(resume_path)