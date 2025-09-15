import os
import csv
import json
import re
from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, JSONResponse, FileResponse
from fastapi.templating import Jinja2Templates
from groq import Groq
from dotenv import load_dotenv
load_dotenv()

app = FastAPI()

# Templates folder with index.html
templates = Jinja2Templates(directory="templates")

# Use env var for API key (run: export GROQ_API_KEY="your-key")
client = Groq(api_key=os.getenv("GROQ_API_KEY"))
CSV_FILE = "call_analysis.csv"

# Ensure CSV exists with headers
if not os.path.exists(CSV_FILE):
    with open(CSV_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Transcript", "Summary", "Sentiment"])


@app.get("/", response_class=HTMLResponse)
def form_page(request: Request):
    """Serve main UI page"""
    return templates.TemplateResponse("index.html", {"request": request})


@app.post("/analyze-ui")
def analyze_ui(transcript: str = Form(...)):
    """Analyze transcript using Groq"""
    prompt = f"""
    You are analyzing a customer support call.

    Transcript: {transcript}

    Summarize in 2–3 sentences and extract sentiment (Positive / Neutral / Negative).

    Respond ONLY in raw JSON, no markdown, no explanation.
    Format:
    {{
      "summary": "...",
      "sentiment": "..."
    }}
    """

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
    )

    raw = response.choices[0].message.content

    # Clean markdown fences if model wraps JSON
    clean = re.sub(r"```(?:json)?|```", "", raw).strip()

    try:
        data = json.loads(clean)
        summary = data.get("summary", "").strip()
        sentiment = data.get("sentiment", "").strip()
    except Exception:
        summary, sentiment = raw.strip(), "Unknown"

    # Save to CSV
    with open(CSV_FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([transcript, summary, sentiment])

    return JSONResponse(
        {"transcript": transcript, "summary": summary, "sentiment": sentiment}
    )


@app.get("/download")
def download_csv():
    """Download analysis CSV"""
    return FileResponse(
        CSV_FILE,
        media_type="text/csv",
        filename="call_analysis.csv",
    )
