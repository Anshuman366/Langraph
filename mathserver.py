from mcp.server.fastmcp import FastMcp

mcp=FastMcp("Math")

@mcp.tool()
def add(a:int,b:int)->int:
    """__summary__
    Add 2 numbers
    """
    return a+b

@mcp.tool()
def multiply(a:int,b:int)->int:
    """__summary__
    Multiply 2 numbers
    """
    return a*b


if __name__=="__main__":
    mcp.run(transport="stdio")
