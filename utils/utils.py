from datetime import date, datetime


def get_new_booking_id():
    return 'sample-booking-id'


def parse_date(date_str: str) -> date:
    return datetime.strptime(date_str, '%Y-%m-%d').date()
