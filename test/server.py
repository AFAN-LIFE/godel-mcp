from fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("Demo")

@mcp.tool()
def mul(a: int, b: int) -> int:
    """multiply two numbers"""
    return a * b

if __name__ == "__main__":
    mcp.run()