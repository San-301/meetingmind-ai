from mcp.server.fastmcp import FastMCP

mcp = FastMCP("MeetingMind")

@mcp.tool()
def generate_report(text: str) -> str:
    """
    Generate a meeting report.
    """
    return text

if __name__ == "__main__":
    mcp.run()