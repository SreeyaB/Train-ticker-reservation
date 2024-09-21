from flask import Flask, request, jsonify

app = Flask(__name__)

# Initializing seats: 0 for available, 1 for booked
seats = [0] * 80

# Pre-booked seats for demonstration
pre_booked_seats = [1, 5, 10, 11, 15, 20, 22, 50, 55, 70]
for seat in pre_booked_seats:
    seats[seat] = 1  # Marking pre-booked seats

@app.route('/')
def home():
    """Welcome message for the seat reservation system."""
    return "Welcome to the Train Seat Reservation System!"

def find_available_seats(count):
    """Find available seats, prioritizing booking in one row first."""
    for row in range(0, 80, 7):
        row_seats = seats[row:row + 7]
        if row_seats.count(0) >= count:  # Enough seats in this row
            return [row + i for i in range(7) if row_seats[i] == 0][:count]
    return [i for i in range(80) if seats[i] == 0][:count] if sum(1 for seat in seats if seat == 0) >= count else None

@app.route('/book', methods=['POST'])
def book_seats():
    """Book the requested number of seats."""
    count = request.json.get('seats', 0)

    # Validate input
    if count < 1 or count > 7:
        return jsonify({'error': 'You can book 1 to 7 seats only.'}), 400

    available_seats = find_available_seats(count)

    # If seats are available, book them
    if available_seats:
        for seat in available_seats:
            seats[seat] = 1  # Mark seat as booked
        return jsonify({'booked_seats': available_seats, 'current_seat_status': seats}), 200
    return jsonify({'error': 'Not enough available seats.'}), 400

@app.route('/status', methods=['GET'])
def get_status():
    """Get the current seat availability status."""
    return jsonify({'current_seat_status': seats}), 200

if __name__ == '__main__':
    app.run(debug=True)
