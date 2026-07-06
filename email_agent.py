from config.gemini import client

def generate_email(summary, actions):
    prompt = f"""
    You are an AI Meeting Assistant.

    Using the meeting summary and action items below, draft a professional
    follow-up email.

    Include:
    - Subject
    - Greeting
    - Summary
    - Action Items
    - Closing

    Meeting Summary:
    {summary}

    Action Items:
    {actions}
    """

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    return response.text