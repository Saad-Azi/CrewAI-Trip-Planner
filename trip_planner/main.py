from crewai import Crew, Process
from agents import TripAgent
from tasks import TripTasks

agents = TripAgent()
tasks = TripTasks()

instructions = input("Enter your current country, destination country, and the duration of your visit including date range: ")

agents_list = [
    agents.country_explorer_agent(),
    agents.city_explorer_agent(),
    agents.expenses_tracker_agent(),
    agents.trip_planner_agent()
]

tasks_list = [
    tasks.country_explorer_task(agent=agents_list[0]),
    tasks.city_explorer_task(agent=agents_list[1]),
    tasks.expenses_tracker_task(agent=agents_list[2]),
    tasks.trip_planner_task(agent=agents_list[3])
]

trip_crew = Crew(
    agents=agents_list,
    tasks=tasks_list,
    process=Process.sequential,
    verbose=True
)

try:
    plan = trip_crew.kickoff(inputs={"instructions": instructions})
    print(plan)
except Exception as e:
    print(f"An error occurred: {e}")
