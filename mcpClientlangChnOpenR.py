# mcpClientlangChnOpenR.py

import os
import asyncio

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

from langchain_mcp_adapters.tools import load_mcp_tools
from langchain.agents import create_agent
from langchain_openai import ChatOpenAI


async def main():
    server_params = StdioServerParameters(
        command="python",
        args=["mcp1.py"],  # 👈 UPDATE THIS
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            # Initialize MCP connection
            await session.initialize()

            # Load MCP tools
            tools = await load_mcp_tools(session)

            # OpenRouter + free Mistral
            llm = ChatOpenAI(
                model="mistralai/mistral-7b-instruct:free",
                base_url="https://openrouter.ai/api/v1",
                api_key= "*****",
                temperature=0,
            )

            # Create agent
            agent = create_agent(llm, tools)

            # Run agent
            response = await agent.ainvoke(
                {"messages": "what's (3 + 5) x 12?"}
            )

            print("\nAgent response:\n", response)


if __name__ == "__main__":
    asyncio.run(main())
