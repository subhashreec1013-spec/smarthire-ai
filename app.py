from flask import Flask, request, jsonify, render_template
import google.generativeai as genai
import os

app = Flask(__name__)

# SET YOUR API KEY HERE
genai.configure(api_key="AIzaSyC_Y7ArDb9aLXhquLjg2rkkAM1ejiKLTNk")

model = genai.GenerativeModel("gemini-pro")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/analyze", methods=["POST"])
def analyze_resume():
    resume_text = request.form.get("resume")
    job_desc = request.form.get("job_description")

    prompt = f"""
You are an AI HR assistant.

Compare the following resume with the job description.

Resume:
{resume_text}

Job Description:
{job_desc}

Return result in this format:

Match Score: %
Matched Skills:
Missing Skills:
Short Explanation:
"""

    response = model.generate_content(prompt)
    result = response.text

    return render_template("result.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
