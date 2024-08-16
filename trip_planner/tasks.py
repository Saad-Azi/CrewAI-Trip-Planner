from crewai import Task
from textwrap import dedent

# create a class for tasks
class TripTasks():
    # create a function for each task
    def country_explorer_task(self,agent):
        return Task(
            description=dedent(
                """\
                From the given query: {instructions}, identify the destination country.
                Utilize the provided tool to compile a list of cities within that country which are ideal for tourists. Include cities with historical sites, charming locations, hidden gems, and entertaining activities.
                """
            ),
            expected_output="List of cities to visit in the destination country.",
            agent=agent
        )
    

    def city_explorer_task(self,agent):
        return Task(
            description=dedent(
            """\
            Given a list of cities, use the tool to identify notable places to visit in each city. Include historical sites, charming locations, hidden gems, and entertaining spots, along with their addresses. Check for any ongoing events during the specified date range in the query: {instructions}, and factor in the forecasted weather for each city.
            """,
            ),
            expected_output="List of places to visit with addresses, including any ongoing events and weather considerations.",
            agent=agent
        )
    
    def expenses_tracker_task(self,agent):
        return Task(
            description=dedent(
            """\
            Use the provided tool to calculate all trip expenses. This includes airfare, taxi fares, meals (breakfast, lunch, dinner), entry fees for attractions, and hotel costs. You have details of the destination country, places to visit, and their addresses.
            """,
        ),
            expected_output="Detailed list of trip expenses, including airfare, taxis, meals, entry fees, and hotel costs.",
            agent=agent
        )
    
    def trip_planner_task(self,agent):
        return Task(
            description=dedent(
            """\
            Using the provided details of the country, cities, places, and expenses, create a comprehensive trip plan according to the timeline specified in {instructions}. Ensure the plan includes:
            - Optimal cities and places to visit
            - Complete expense breakdown (airfare, intercity travel, meals, entry fees, hotel)
            - Exciting activities for each location
            - Include any notes if necessary regarding weather conditions or any notable things.
            Stay within the timeline and use the tool to fill in any missing details.
            """,
        ),
            expected_output="A detailed trip plan including cities, places, activities,notes and a complete expense breakdown.",
            agent=agent
        )
    

