from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_community.tools import tool
from dotenv import load_dotenv

load_dotenv()

@tool("Calculate")
def Calculate(expression):
    """Use this tool to calculate the expenses safely. This tool only excepts a mathematical expression."""
    try:
        result = eval(expression, {"__builtins__": None}, {})
        return result
    except Exception as e:
        return f"Error in calculation: {e}"

search_tool=TavilySearchResults()