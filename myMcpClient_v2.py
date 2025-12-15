import asyncio
import os 

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

from langchain_mcp_adapters.tools import load_mcp_tools
from langchain.agents import create_agent

# Set API key
#os.environ['OPENAI_API_KEY'] = '*****'
os.environ['GEMINI_API_KEY'] = '*****'


async def main():
    server_params = StdioServerParameters(
        command="python",
        # Use absolute path if needed
        args=["mcp1.py"],
        
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # Initialize MCP connection
            await session.initialize()

            # Load MCP tools
            tools = await load_mcp_tools(session)

            # Create and run agent
            #agent = create_agent("openai:gpt-4.1", tools)
            agent = create_agent("gemini-2.5-flash", tools)
            response = await agent.ainvoke(
                {"messages": "what's (3 + 5) x 12?"}
            )

            print(response)


if __name__ == "__main__":
    asyncio.run(main())
