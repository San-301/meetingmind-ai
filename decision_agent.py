from config.gemini import client

def extract_decisions(transcript: str):
    prompt = f"""
    You are an AI Meeting Decision Agent.

    Read the meeting transcript and extract ONLY the decisions made.

    Format:
    - Decision 1
    - Decision 2
    - Decision 3

    If no decisions were made, say:
    "No major decisions were made."

    Transcript:
    {transcript}
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text