# SmartHire AI

Intelligent Resume Screening & HR Automation using NLP

Hackathon Project – SRM Noob Hackfest 2026

---

## Overview
SmartHire AI is a web-based platform that uses Artificial Intelligence and Natural Language Processing (NLP) to automatically analyze resumes and match them with job descriptions. It helps recruiters shortlist candidates faster, more accurately, and in a bias-free manner.

---

## Live Workflow
Resume Input → AI Analysis (Gemini) → Match Score & Skill Comparison → Candidate Insight

---

## System Architecture

Frontend (HTML / CSS / JavaScript)  
&nbsp;&nbsp;&nbsp;&nbsp;↓  
Flask Backend API (Python)  
&nbsp;&nbsp;&nbsp;&nbsp;↓  
Google Gemini AI Model  
&nbsp;&nbsp;&nbsp;&nbsp;↓  
Analysis Results (Score, Skills, Explanation)

---

## Problem Statement
Recruiters receive hundreds of resumes for a single job role, making manual screening slow, inconsistent, and prone to bias. Traditional Applicant Tracking Systems rely mainly on keyword matching and often reject qualified candidates due to formatting or wording differences.

---

## Our Solution
SmartHire AI extracts skills, education, and experience from resumes, performs semantic matching with job requirements, generates explainable match scores, highlights skill gaps, and ranks candidates based on relevance using AI.

---

## Key Features
- Web-based resume analyzer  
- NLP-based skill extraction  
- Semantic job matching using AI  
- Explainable AI scoring  
- Skill gap analysis with learning suggestions  
- Candidate ranking dashboard  
- Bias-free screening mode  
- Recruiter-customizable scoring weights  

---

## Technology Stack
- Frontend: HTML, CSS, JavaScript  
- Backend: Python (Flask)  
- AI / NLP: Google Gemini API (`gemini-flash-latest`)  
- Resume Parsing: PyPDF2 / pdfplumber (planned)  
- Database: SQLite / Firebase (optional)

---

## Impact
- Reduces resume screening time by up to 80%  
- Improves fairness and transparency in hiring  
- Enhances candidate–job matching accuracy  
- Useful for startups, HR teams, and campus placements  

---

## Team

**Team Name:** Hack Nova

**Members:**
- Subha Shree C  
- Shiyam Shankar  
- Sundhares  
- Abdul Wahid S  
- Mohammed Saad M  

---

## Status
Project under development for SRM Noob Hackfest 2026.

---

## AI-Powered Web Demo

This project includes a Flask-based web application integrated with Google's Gemini AI for semantic resume–job matching.

### Features
- Web UI for resume & job description input  
- AI-based semantic analysis using Gemini  
- Match score, matched skills, missing skills, and explanation  
- End-to-end working prototype  

### How to run locally

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
