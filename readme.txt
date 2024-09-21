
# Train Seat Reservation System

## Overview
The Train Seat Reservation System is a web application developed using Flask that allows users to reserve seats in a train coach. The system is designed to facilitate the booking of seats while prioritizing row-wise allocation and ensuring efficient seat management.

## Features
- Seat Reservation: Users can reserve up to 7 seats at a time.
- **Row Priority Booking**: Seats are booked in a row first; if not enough seats are available in a single row, nearby seats are allocated.
- **Real-time Availability**: Users can check the current status of seat availability.

## Seating Arrangement
- The train coach has a total of 80 seats arranged as follows:
  - Rows 1-10: 7 seats per row
  - Last row (Row 11): 3 seats

## Getting Started

### Prerequisites
- Python 3.x
- Flask

### Installation Steps

1. Clone the repository (if using Git) or download the `app.py` file.
2. **Install Flask** using pip:
   ```bash
   pip install Flask
Running the Application
Open your terminal and navigate to the directory containing app.py.
Start the application by running:
bash
Copy code
python app.py


Copy code
http://127.0.0.1:5000/
API Endpoints
1. Home Endpoint
Method: GET
Endpoint: /
Description: Displays a welcome message.
Response:
json
Copy code
"Welcome to the Train Seat Reservation System!"
2. Book Seats
Method: POST
Endpoint: /book
Request Body: JSON format
json
Copy code
{
  "seats": <number_of_seats>
}
Description: Books the specified number of seats (1 to 7).
Success Response:
json
Copy code
{
  "booked_seats": [0, 1],
  "current_seat_status": [1, 1, 0, ...]
}
Error Response:
json
Copy code
{
  "error": "Not enough available seats."
}
3. Check Seat Availability
Method: GET
Endpoint: /status
Description: Retrieves the current seat availability status.
Response:
json
Copy code
{
  "current_seat_status": [0, 1, 1, 0, ...]
}
Usage Example with Postman
To test the application, you can use Postman to send requests to the API endpoints:

For booking seats, send a POST request to /book with the JSON body:
http://127.0.0.1:5000/post
json
Copy code
{
  "seats": 2
}
To check seat availability, send a GET request to /status.

http://127.0.0.1:5000/post
http://127.0.0.1:5000/status


Assumptions
Users can only book seats when there are available seats.
No login functionality is required for this application.