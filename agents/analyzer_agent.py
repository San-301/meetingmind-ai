from config.gemini import client
import json


def analyze_meeting(transcript: str):

    prompt = f"""
You are MeetingMind AI.

Analyze the following meeting transcript.

Return ONLY valid JSON in this exact format:

{{
    "summary": "...",
    "decisions": [
        "..."
    ],
    "action_items": [
        {{
            "person": "...",
            "task": "...",
            "deadline": "...",
            "priority": "..."
        }}
    ],
    "email": "...",
    "schedule": "..."
}}

Instructions:

1. If there are no decisions, return:
"decisions": ["No decisions identified."]

2. If there are no action items, return:
"action_items": [
    {{
        "person": "Not Available",
        "task": "No action items identified.",
        "deadline": "N/A",
        "priority": "N/A"
    }}
]

3. Always generate a professional follow-up email, even if the meeting was only informational.

4. Always suggest a follow-up schedule based on the meeting context.

5. Return ONLY JSON.

6. Do NOT use markdown.

7. Do NOT wrap the response in ```json.

Meeting Transcript:
{transcript}
"""

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    text = response.text.strip()

    if text.startswith("```json"):
        text = text.replace("```json", "").replace("```", "").strip()
    elif text.startswith("```"):
        text = text.replace("```", "").strip()

    return json.loads(text)