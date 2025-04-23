import asyncio
from fastmcp import FastMCP, Client

mcp = FastMCP("My MCP Server")

@mcp.tool()
def mul(a: int, b: int) -> int:
    """multiply two numbers"""
    return a * b

client = Client(mcp)

async def call_tool(a: int, b: int):
    async with client:
        result = await client.call_tool("mul", {"a": a, "b": b})
        print(result)

asyncio.run(call_tool(3, 4))


async def main():
    async with client:
        tools = await mcp.get_tools()  # 正确await异步方法
        print(tools)

asyncio.run(main())