from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("bilka")

# Constants
API_BASE = "https://api.example.com"  # Replace with your API base URL
USER_AGENT = "bilka-mcp/1.0"

async def make_api_request(url: str) -> dict[str, Any] | None:
    """Make a request to the API with proper error handling."""
    headers = {
        "User-Agent": USER_AGENT,
        "Accept": "application/json"
    }
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, headers=headers, timeout=30.0)
            response.raise_for_status()
            return response.json()
        except Exception as e:
            print(f"Error making API request: {e}")
            return None

@mcp.tool()
async def example_tool(param: str) -> str:
    """Example tool that demonstrates MCP functionality.
    
    Args:
        param: Example parameter
        
    Returns:
        str: Example response
    """
    # Replace with your actual API endpoint
    url = f"{API_BASE}/endpoint?param={param}"
    data = await make_api_request(url)
    
    if not data:
        return "Unable to fetch data from the API."
    
    # Process and return the data
    return str(data)

if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport='stdio') 