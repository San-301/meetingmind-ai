from google.adk.agents import Agent
from agents.analyzer_agent import analyze_meeting


def analyze_tool(transcript: str):
    return analyze_meeting(transcript)


meetingmind_agent = Agent(
    name="MeetingMindAI",
    model="gemini-2.5-flash",
    description="AI Meeting Assistant",
    instruction="""
You are MeetingMind AI.

Analyze meetings and return:
- Summary
- Decisions
- Action Items
- Email
- Schedule
""",
    tools=[analyze_tool],
)