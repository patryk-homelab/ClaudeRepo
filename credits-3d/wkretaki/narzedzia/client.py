import asyncio, os, sys, json
from mcp import ClientSession
from mcp.client.stdio import StdioServerParameters, stdio_client
async def main():
    p = StdioServerParameters(command="build123d-mcp", args=[], env=dict(os.environ), cwd=os.getcwd())
    async with stdio_client(p) as (r, w):
        async with ClientSession(r, w) as s:
            await s.initialize()
            if sys.argv[1] == "list":
                t = await s.list_tools()
                for x in t.tools: print(x.name, "|", (x.description or "")[:150].replace("\n", " "), "|", list((getattr(x, "input_schema", None) or getattr(x, "inputSchema", None) or {}).get("properties", {}).keys()))
            else:
                for call in json.loads(open(sys.argv[1]).read()):
                    res = await s.call_tool(call["tool"], call.get("args", {}))
                    txt = " ".join(getattr(c, "text", "") or "" for c in res.content)
                    print("==", call["tool"], "->", txt[:3000])
asyncio.run(main())
