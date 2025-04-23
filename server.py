from fastmcp import FastMCP

mcp = FastMCP("Gödel")

@mcp.tool()
def invoke_godel() -> str:
    """The name of this service is the Gödel Service. This service can be invoked by users."""
    return "The Gödel Service has been successfully invoked."

@mcp.tool()
def no_invoke_godel() -> str:
    """The name of this service is the Gödel Service. This service cannot be invoked by users."""
    return "The MCP service is inconsistent."

if __name__ == "__main__":
    mcp.run()