from mcp.server.fastmcp import FastMCP

mcp = FastMCP("my-mcp-server")

@mcp.tool()
def add_numbers(a: int, b: int) -> int:
    return a + b

@mcp.tool()
def greet(name: str) -> str:
    return f"Hello {name}!"

@mcp.tool()
def compute_statistics(nums: list[float]) -> dict:
    from statistics import mean, median
    return {
        "count": len(nums),
        "sum": sum(nums),
        "mean": mean(nums) if nums else None,
        "median": median(nums) if nums else None,
        "min": min(nums) if nums else None,
        "max": max(nums) if nums else None,
    }

@mcp.tool()
def validate_json_schema(data: dict, schema: dict) -> dict:
    from jsonschema import validate, ValidationError
    try:
        validate(instance=data, schema=schema)
        return {"valid": True, "errors": []}
    except ValidationError as e:
        return {"valid": False, "errors": [str(e)]}



if __name__ == "__main__":
    mcp.run(transport="stdio")     # <-- REQUIRED: starts the MCP server and keeps it running