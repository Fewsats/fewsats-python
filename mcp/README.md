# MCP server for Fewsats

## Usage

Copy `.env.example` to `.env` and set the `FEWSATS_API_KEY` environment variable.

### Claude Desktop App

To install the MCP server for use with the Claude desktop app:

```bash
mcp install main.py --name 'Fewsats MCP' --env-file .env
```

This will add the server to `$HOME/Library/Application Support/Claude/claude_desktop_config.json` so Claude can access it directly.

You can ask Claude "what tools are available?" to see the list of Fewsats tools.



## Debug 

To try out the tools:

```
pip install -r requirements.txt
mcp dev main.py
```

Open the inspector and use the tools. 




