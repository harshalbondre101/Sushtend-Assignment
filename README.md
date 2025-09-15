# Call Transcript Analyzer

A web app that analyzes customer support call transcripts using the Groq API. It summarizes conversations, detects sentiment, and stores results in a CSV file. Built with FastAPI, Tailwind CSS, and the Groq Chat Completions API.

## Features

Input a transcript (or paste multiple lines of a call).

Returns a summary in 2–3 sentences.

Detects customer sentiment: Positive, Neutral, Negative.

Saves all analyses to call_analysis.csv.

Download CSV from the UI.

Modern, responsive design with Tailwind CSS.

### Prerequisites

Python 3.10+

Groq API key

pip package manager

### Setup

Clone the repo

git clone <your-repo-url>
cd <repo-folder>


### Create a virtual environment (optional but recommended)

python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows


### Install dependencies

pip install fastapi uvicorn jinja2 groq python-dotenv


Create a .env file in the project root:

GROQ_API_KEY="your_groq_api_key_here"

### Project Structure
project/
│── app.py                  # FastAPI backend
│── templates/
│     └── index.html        # Tailwind CSS frontend
│── call_analysis.csv       # Generated CSV file (created automatically)
│── .env                    # Groq API key

### Running the App
uvicorn app:app --reload


Open your browser at http://127.0.0.1:8000

Paste a transcript → click Analyze Transcript

View summary and sentiment on the same page

Download CSV using 📥 Download CSV button

## Usage Example

Transcript Input:

Customer: Hi, I tried booking a slot yesterday for your service, but the payment failed.
Agent: I’m sorry to hear that. Did you receive any error message?
Customer: Yes, it said "transaction declined" even though my card works elsewhere.
Agent: I understand. I’ll escalate this to our billing team and ensure your slot is reserved.
Customer: Thanks, I was really frustrated because I needed it urgently.


Output:

Summary: A customer attempted to book a service but the payment failed. The agent promised to escalate the issue and reserve the slot.

Sentiment: Negative

## Notes

Always store your GROQ_API_KEY securely; never commit .env to public repos.

Tailwind CSS is loaded via CDN — no additional setup required.

CSV file is automatically created on first run.

### Future Improvements

Upload audio recordings for transcription using Groq’s Whisper models.

Add multiple sample transcripts to quickly test positive/neutral/negative cases.

Real-time updates while analyzing long transcripts.
