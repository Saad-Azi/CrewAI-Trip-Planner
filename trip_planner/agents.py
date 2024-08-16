from crewai import Agent
from textwrap import dedent
from tools import search_tool,Calculate
from langchain_openai.chat_models import ChatOpenAI
from dotenv import load_dotenv

# Load environment variables from a .env file
load_dotenv()
# Initialize the OpenAI language model with the GPT-4o-mini configuration
llm=ChatOpenAI(model="gpt-4o-mini")

# create class for agents
class TripAgent():
    # create a function for each agent
    def country_explorer_agent(self):
        return Agent(
            role="Experienced country explorer",
            goal="Guide customers on exploring charming and fun places in each city of a country.",
            backstory=dedent(
                """\
                An experienced traveler with extensive knowledge of every country on Earth. Dedicated to exploring and understanding global destinations.
                """
            ),
            tools=[search_tool],    # Tool used for searching information about countries
            llm=llm,                # Language model used for generating responses
            verbose=True
        )
    
    def city_explorer_agent(self):
        return Agent(
            role="Experienced city explorer",
            goal="Guide customers to explore all charming and notable places in a city.",
            backstory=dedent(
                """\
                A seasoned traveler with comprehensive knowledge of every city worldwide. Expertise in finding and recommending the best places to visit in each city.
                """
            ),
            tools=[search_tool],    # Tool used for searching information about countries
            llm=llm,                # Language model used for generating responses
            verbose=True
        )
    
    def expenses_tracker_agent(self):
        return Agent(
            role="Finance Expert",
            goal="Accurately predict and calculate trip expenses.",
            backstory=dedent(
                """\
                A finance expert with over 10 years of experience in trip expense forecasting. Known for 99.99% accuracy. Focus on numeric calculations only; currency does not matter.
                """
            ),
            tools=[Calculate,search_tool],  # Tool used for searching information about countries
            llm=llm,                        # Language model used for generating responses
            verbose=True
        )

    def trip_planner_agent(self):
        return Agent(
            role="Expert Trip Advisor",
            goal="Plan trips considering time, cities, and expense tracking.",
            backstory=dedent(
                """\
                An expert trip planner with over 10 years of experience, dedicated to creating optimal travel plans. You aim to provide exceptional service to maximize customer satisfaction.
                """
            ),
            tools=[search_tool],    # Tool used for searching information about countries
            llm=llm,                # Language model used for generating responses
            verbose=True
        )