from inspect import signature, getdoc
from sherlock.core import Sherlock
from textwrap import dedent

def generate_mcp_tools():
    s = Sherlock()
    tools = s.as_tools()
    
    header = '''
    from fastmcp import FastMCP
    from sherlock.core import Sherlock
    import os

    # Create FastMCP and Sherlock instances
    mcp = FastMCP("Sherlock Domains MCP Server")
    s = Sherlock()
    '''
    
    tool_template = '''
    @mcp.tool()
    async def {name}({params}) -> str:
        """{docstring}"""
        return str(s.{name}({args}))
    '''
    
    footer = '''
    if __name__ == "__main__":
        mcp.run()
    '''
    
    generated_code = [dedent(header)]
    
    for tool_func in tools:
        tool_name = tool_func.__name__
        sig = signature(tool_func)
        params = ', '.join(f"{p}: {v.annotation.__name__ if hasattr(v.annotation, '__name__') else 'str'}" 
                         for p, v in sig.parameters.items())
        args = ', '.join(p for p in sig.parameters)
        docstring = getdoc(tool_func) or f"{tool_name} function"
        
        tool_code = dedent(tool_template).format(
            name=tool_name,
            params=params,
            docstring=docstring,
            args=args
        )
        generated_code.append(tool_code)
    
    generated_code.append(dedent(footer))
    
    with open('main.py', 'w') as f:
        f.write('\n'.join(generated_code))

if __name__ == "__main__":
    generate_mcp_tools()
