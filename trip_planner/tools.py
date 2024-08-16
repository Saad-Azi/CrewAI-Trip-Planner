from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_community.tools import tool
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()

# create custom tool with a tool decorator from langchain
@tool("Calculate")
def Calculate(expression):
    """Use this tool to calculate the expenses safely. This tool only excepts a mathematical expression."""
    try:
        result = eval(expression, {"__builtins__": None}, {})
        return result
    except Exception as e:
        return f"Error in calculation: {e}"

# create an instance of Tavily tool
search_tool=TavilySearchResults()