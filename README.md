# Bilka MCP Server

An MCP server for integrating with public APIs.

## Setup

1. Install `uv` if you haven't already:
   ```bash
   curl -LsSf https://astral.sh/uv/install.sh | sh
   ```

2. Create and activate a virtual environment:
   ```bash
   uv venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   uv add "mcp[cli]" httpx
   ```

## Running the Server

To run the server:
```bash
python src/server.py
```

## Configuration

The server can be configured by modifying the constants in `src/server.py`:
- `API_BASE`: The base URL for the API you're integrating with
- `USER_AGENT`: The user agent string to use for API requests

## Adding New Tools

To add new tools to the server:
1. Create a new async function in `src/server.py`
2. Decorate it with `@mcp.tool()`
3. Add proper type hints and docstrings
4. Implement the tool's functionality

## Testing with Claude for Desktop

To use this server with Claude for Desktop, add the following to your `claude_desktop_config.json`:

```json
{
    "mcpServers": {
        "bilka": {
            "command": "python",
            "args": [
                "src/server.py"
            ]
        }
    }
}
```
