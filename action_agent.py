from config.gemini import client

def extract_action_items(transcript: str):
    prompt = f"""
    You are an AI Action Item Agent.

    Extract all action items from the meeting.

    For each action item provide:

    - Person Responsible
    - Task
    - Deadline (if mentioned)
    - Priority (High/Medium/Low)

    Return as a markdown table.

    Transcript:
    {transcript}
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text