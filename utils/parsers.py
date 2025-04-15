from datetime import datetime, date

from models.booking import Booking
from models.car import Car


def parse_date(date_str: str) -> date:
    return datetime.strptime(date_str, '%Y-%m-%d').date()


def parse_car(car_data: dict) -> Car:
    return Car(
        id=car_data['id'],
        make=car_data['make'],
        model=car_data['model'],
        color=car_data['color']
    )


def parse_booking(booking_data: dict) -> Booking:
    return Booking(
        id=booking_data['id'],
        car_id=booking_data['carId'],
        start_date=parse_date(booking_data['startDate']),
        end_date=parse_date(booking_data['endDate']),
        booker_id=booking_data['bookerId'],
    )
