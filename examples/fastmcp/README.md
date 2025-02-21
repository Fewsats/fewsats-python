# FastMCP server for Fewsats

## Usage


Copy `.env.example` to `.env` and set the `FEWSATS_API_KEY` environment variable.

### Claude desktop app

```
fastmcp install main.py -f .env
```


This will add the server to `$HOME/Library/Application Support/Claude/claude_desktop_config.json` so it can be used in Claude desktop app directly.

You can ask Claude "what tools are available?" and it will list the tools.

### Cursor

1. Add a new command as explained in [here](https://docs.cursor.com/context/model-context-protocol).
2. Select `type: command`
3. Add the following commmand:
 `env FEWSATS_API_KEY=YOUR_API_KEY uv run --with fastmcp fastmcp run path/to/fewsats-python/examples/fastmcp/main.py`
 3.a. Make sure to replace `YOUR_API_KEY` with your actual API key.
 3.b. Make sure to replace `path/to/fewsats-python/examples/fastmcp/main.py`

## Debug 

To try out the tools:

```
pip install -r requirements.txt
fastmcp dev main.py
```

Open the inspector and use the tools. 




