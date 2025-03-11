#!/bin/bash

# Navigate to the MCP directory
cd /home/albert/git/fewsats-python/mcp

# Load environment variables from .env file
if [ -f ".env" ]; then
    export $(grep -v '^#' ".env" | xargs)
    echo "Environment variables loaded from .env"
else
    echo "Warning: .env file not found"
fi

# Run the MCP server
uv run mcp-server-fewsats