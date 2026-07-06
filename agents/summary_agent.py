from config.gemini import client

def generate_summary(transcript: str):
    prompt = f"""
    You are an expert meeting assistant.

    Analyze the following meeting transcript and generate:

    1. Executive Summary
    2. Key Discussion Points
    3. Important Decisions
    4. Risks (if any)

    Meeting Transcript:
    {transcript}
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text