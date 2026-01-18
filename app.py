from flask import Flask, request, render_template
import os
import google.generativeai as genai

app = Flask(__name__)

@app.route("/")
def home():
    return "SmartHire AI Demo API is running"

@app.route("/analyze", methods=["POST"])
def analyze_resume():
    data = request.json

    resume_text = data.get("resume", "")
    job_desc = data.get("job_description", "")

    resume_words = set(resume_text.lower().split())
    job_words = set(job_desc.lower().split())

    matched = resume_words.intersection(job_words)
    score = int((len(matched) / max(len(job_words), 1)) * 100)

    return jsonify({
        "match_score": score,
        "matched_skills": list(matched),
        "missing_skills": list(job_words - matched),
        "explanation": "Demo response. AI integration will be added during hackathon."
    })
   True)
