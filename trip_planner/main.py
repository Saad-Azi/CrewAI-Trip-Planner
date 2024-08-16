from crewai import Crew, Process
from agents import TripAgent
from tasks import TripTasks

# create an instance of TripAgent class
agents = TripAgent()
# create an instance of TripTasks class
tasks = TripTasks()

# accepting input from the user for trip details
instructions = input("Enter your current country, destination country, and the duration of your visit including date range: ")

# Create a list of agents
agents_list = [
    agents.country_explorer_agent(),  # Agent for exploring destination countries
    agents.city_explorer_agent(),     # Agent for exploring cities
    agents.expenses_tracker_agent(),  # Agent for tracking expenses
    agents.trip_planner_agent()       # Agent for overall trip planning
]

# Create a list of tasks associated with each agent

tasks_list = [
    tasks.country_explorer_task(agent=agents_list[0]),  # Task to identify destination cities
    tasks.city_explorer_task(agent=agents_list[1]),     # Task to provide details about places within cities
    tasks.expenses_tracker_task(agent=agents_list[2]),  # Task to calculate trip expenses
    tasks.trip_planner_task(agent=agents_list[3])       # Task to create a comprehensive trip plan
]

# Create an instance of the Crew with specified agents and tasks
trip_crew = Crew(
    agents=agents_list,
    tasks=tasks_list,
    process=Process.sequential,
    verbose=True
)

# Execute the trip planning process and handle potential errors
try:
    plan = trip_crew.kickoff(inputs={"instructions": instructions})
    print(plan) # print the generated trip plan
except Exception as e:
    print(f"An error occurred: {e}")    # print any occured error
