# Trip Planning Assistant

## Overview

The Trip Planning Assistant is a Python program designed to help users plan their trips efficiently. It utilizes multiple agents to handle different aspects of trip planning, including destination exploration, city exploration, expense tracking, and overall trip planning.

## Features

- **Country Explorer Agent**: Identifies destination countries and highlights interesting cities and places to visit.
- **City Explorer Agent**: Provides detailed information about places to visit within a city.
- **Expenses Tracker Agent**: Calculates and predicts the expenses for the trip, including airfare, transportation, meals, and more.
- **Trip Planner Agent**: Creates a comprehensive trip plan considering time constraints, cities to explore, and expense tracking.

## Installation

To use this program, ensure you have Python 3.11.7 installed. You also need to install the required dependencies. You can do this using `poetry`:

```bash
poetry install
poetry run python main.py
```
# Example input
Enter your current country and destination country along with the time duration of your visit:
I am currently in Pakistan and planning a 7-day trip to France from August 17, 2024, to August 24, 2024.

# Example output
### Comprehensive Trip Plan to France (17 August 2024 - 24 August 2024)

**Day 1: Arrival in Paris (17 August 2024)**
- **Activities**: Arrive at Charles de Gaulle Airport. Take a taxi to the hotel. Spend the day relaxing and getting over jet lag. If time permits, take a leisurely evening stroll around the Seine River.
- **Meals**: Dinner at a local bistro.
- **Expenses**:
  - Airfare: $1000
  - Taxi Fare: $55 (to hotel)
  - Meals: $45

**Day 2: Explore Paris (18 August 2024)**
- **Activities**:
  - Morning: Visit the Eiffel Tower (Entry Fee: $20).
  - Afternoon: Explore the Louvre Museum (Entry Fee: $17).
  - Evening: Take a Seine River cruise to see the city lights.
- **Meals**: Breakfast and lunch at local cafés, dinner at a restaurant.
- **Expenses**:
  - Entry Fees: $37
  - Meals: $135
  - Taxi Fare: $55 (for the day)

**Day 3: Day Trip to Versailles (19 August 2024)**
- **Activities**:
  - Morning: Visit the Palace of Versailles (Entry Fee: $20).
  - Afternoon: Explore the gardens and enjoy a picnic lunch.
  - Evening: Return to Paris.
- **Meals**: Breakfast at the hotel, picnic lunch, dinner in Paris.
- **Expenses**:
  - Entry Fees: $20
  - Meals: $135
  - Taxi Fare: $55 (to and from Versailles)

**Day 4: Travel to Lyon (20 August 2024)**
- **Activities**:
  - Morning: Take a train to Lyon.
  - Afternoon: Explore the Old Town (Vieux Lyon) and visit Basilica of Notre-Dame de Fourvière (Entry Fee: $8).
  - Evening: Dinner at a local brasserie.
- **Meals**: Breakfast at the hotel, lunch in Lyon, dinner in Lyon.
- **Expenses**:
  - Train Ticket: $50
  - Entry Fees: $8
  - Meals: $135
  - Taxi Fare: $55 (from train station to hotel)

**Day 5: Explore Lyon (21 August 2024)**
- **Activities**:
  - Morning: Bike tour of the city's parks and rivers.
  - Afternoon: Visit Parc de la Tête d'Or.
  - Evening: Enjoy local cuisine at a bouchon.
- **Meals**: Breakfast at the hotel, lunch in the park, dinner at a bouchon.
- **Expenses**:
  - Bike Tour: $30
  - Meals: $135
  - Taxi Fare: $55 (for the day)

**Day 6: Travel to Nice (22 August 2024)**
- **Activities**:
  - Morning: Take a train to Nice.
  - Afternoon: Relax at Promenade des Anglais (No entry fee).
  - Evening: Explore the Old Town and have dinner at a seaside restaurant.
- **Meals**: Breakfast at the hotel, lunch in Nice, dinner in Nice.
- **Expenses**:
  - Train Ticket: $50
  - Meals: $135
  - Taxi Fare: $55 (from train station to hotel)

**Day 7: Day Trip to Monaco (23 August 2024)**
- **Activities**:
  - Morning: Visit Monaco via train.
  - Afternoon: Explore the Prince's Palace and the Oceanographic Museum (Entry Fee: $15).
  - Evening: Return to Nice.
- **Meals**: Breakfast at the hotel, lunch in Monaco, dinner in Nice.
- **Expenses**:
  - Train Ticket: $20
  - Entry Fees: $15
  - Meals: $135
  - Taxi Fare: $55 (for the day)

**Day 8: Depart from Nice (24 August 2024)**
- **Activities**: Last-minute shopping and sightseeing in Nice. Take a taxi to the airport for departure.
- **Meals**: Breakfast at the hotel and lunch at the airport.
- **Expenses**:
  - Taxi Fare: $55
  - Meals: $90

### Total Expense Breakdown:
- **Airfare**: $1000
- **Taxi Fares**: $110
- **Meals**: $1080
- **Entry Fees**: $90
- **Hotel Costs**: $875
- **Train Tickets**: $120
- **Bike Tour**: $30
- **Total Estimated Expenses**: **$3155**

### Notes:
- **Weather**: August in France is typically warm, so pack accordingly with light clothing and sun protection.
- **Events**: The Paris Jazz Festival will be ongoing in August, which you might enjoy attending.
- **Cultural Tips**: Be sure to learn a few basic French phrases to enhance your experience.

Enjoy your trip exploring France's rich history, vibrant culture, and stunning landscapes!
