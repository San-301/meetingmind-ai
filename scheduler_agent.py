from config.gemini import client

def suggest_schedule(summary, actions):
    prompt = f"""
    You are a Meeting Scheduler AI.

    Based on the meeting summary and action items:

    1. Suggest the next meeting date or timeframe.
    2. List milestones before the next meeting.
    3. Mention any dependencies or blockers.
    4. Recommend an agenda for the next meeting.

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