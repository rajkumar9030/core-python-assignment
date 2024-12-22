total_seats = 10
booked_seats = [2, 5, 7]

def book_seat(seat):
    if seat in booked_seats:
        print(f"Seat {seat} is already booked.")
    elif seat < 1 or seat > total_seats:
        print(f"Invalid seat number: {seat}. Please choose a seat between 1 and {total_seats}.")
    else:
        booked_seats.append(seat)
        print(f"Seat {seat} has been booked.")

def cancel_seat(seat):
    if seat in booked_seats:
        booked_seats.remove(seat)
        print(f"Seat {seat} has been canceled.")
    else:
        print(f"Seat {seat} was not booked.")

def available_seats():
    all_seats = set(range(1, total_seats + 1))
    booked_set = set(booked_seats)
    available = sorted(list(all_seats - booked_set))
    return available

book_seat(3)
cancel_seat(5)
print("Available seats:", available_seats())
