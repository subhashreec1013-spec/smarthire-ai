from flask import Flask, request, render_template_string
import os
import google.generativeai as genai

# Configure Gemini API
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html>
<head>
    <title>SmartHire AI</title>
    <style>
        body { font-family: Arial; background:#f4f6f8; padding:40px; }
        textarea { width:100%; height:120px; margin-top:10px; }
        button { padding:10px 20px; margin-top:15px; background:#007bff; color:white; border:none; }
        .box { background:white; padding:25px; border-radius:8px; max-width:800px; margin:auto; }
        pre { background:#eee; padding:15px; }
    </style>
</head>
<body>
<div class="box">
<h2>SmartHire AI – Resume Screening</h2>

<form method="post">
<label>Resume Text:</label>
<textarea name="resume" required></textarea>

<label>Job Description:</label>
<textarea name="job" required></textarea>

<button type="submit">Analyze</button>
</form>

{% if result %}
<h3>AI Result:</h3>
<pre>{{ result }}</pre>
{% endif %}
</div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        resume = request.form["resume"]
        job = request.form["job"]

        prompt = f"""
You are an AI recruitment assistant.

Compare this resume with the job description.
Give:
1. Match percentage
2. Missing skills
3. Strengths
4. Final hiring recommendation

Resume:
{resume}

Job Description:
{job}
"""

        try:
            model = genai.GenerativeModel("gemini-pro")
            response = model.generate_content(prompt)
            result = response.text
        except Exception as e:
            result = f"Error: {str(e)}"

    return render_template_string(HTML_PAGE, result=result)


if __name__ == "__main__":
    app.run(debug=True)
