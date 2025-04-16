from datetime import date, datetime

from crud.crud import get_all_bookings


def get_new_booking_id():
    booking_numbers = [int(booking.id.split('-')[-1]) for booking in get_all_bookings()]
    new_number = max(booking_numbers) + 1

    return f'booking-{new_number:02}'


def parse_date(date_str: str) -> date:
    return datetime.strptime(date_str, '%Y-%m-%d').date()
