# 🧠 MeetingMind AI

> AI-powered Multi-Agent Meeting Assistant built using Google Gemini, Google ADK, MCP, and Streamlit.

---

## 📌 Problem Statement

Professionals spend significant time manually summarizing meetings, identifying action items, preparing follow-up emails, and scheduling next meetings. This process is repetitive, time-consuming, and prone to missed information.

MeetingMind AI automates these tasks using AI agents, enabling teams to focus on execution instead of documentation.

---

## 🚀 Features

- 📄 Meeting Summary
- ✅ Decision Extraction
- 📋 Action Item Identification
- 📧 Follow-up Email Generation
- 📅 Schedule Suggestions
- 📑 PDF Report Generation
- 📂 Support for TXT, PDF, DOCX
- ⚡ Interactive Streamlit Dashboard

---

## 🏗 Architecture

User Upload
↓
Streamlit UI
↓
Coordinator Agent
↓
Meeting Analyzer (Gemini)
↓
Structured JSON
↓
Summary | Decisions | Actions | Email | Schedule
↓
PDF Generator

---

## 🛠 Tech Stack

- Python
- Streamlit
- Google Gemini 2.5 Flash
- Google ADK
- MCP
- ReportLab
- PyPDF
- python-docx

---

## 📂 Project Structure

```text
meetingmind-ai/
│
├── agents/
├── config/
├── tools/
├── outputs/
├── uploads/
├── app.py
├── README.md
└── requirements.txt
```

---

## ⚙ Installation

```bash
git clone <repo>

cd meetingmind-ai

pip install -r requirements.txt

streamlit run app.py
```

---

## 📸 Demo

Upload a meeting document.

MeetingMind AI automatically generates:

- Executive Summary
- Decisions
- Action Items
- Follow-up Email
- Schedule
- Downloadable PDF Report

---

## 🔒 Security

- API keys stored using `.env`
- No hardcoded credentials
- Local processing for uploaded files

---

## 🔮 Future Improvements

- Whisper Audio Transcription
- Google Calendar Integration
- Gmail Integration
- Slack Integration
- Meeting Chat Assistant
- Multi-language Support

---

## 👨‍💻 Team

Builder_of_AI