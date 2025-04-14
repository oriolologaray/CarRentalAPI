import json
from datetime import date, datetime

from models.booking import Booking
from models.car import Car

CARS_DB_PATH = 'test_data/cars.json'
BOOKINGS_DB_PATH = 'test_data/bookings.json'


def get_all_cars() -> list[Car]:
    with open(CARS_DB_PATH, 'r') as file:
        data = json.load(file)

    return [parse_car(car) for car in data]


def get_all_bookings() -> list[Booking]:
    with open(BOOKINGS_DB_PATH, 'r') as file:
        data = json.load(file)

    return [parse_booking(booking) for booking in data]


def parse_date(date_str: str) -> date:
    return datetime.strptime(date_str, '%d-%m-%Y').date()


def parse_booking(booking_data: dict) -> Booking:
    return Booking(
        id=booking_data['id'],
        car_id=booking_data['carId'],
        start_date=parse_date(booking_data['startDate']),
        end_date=parse_date(booking_data['endDate']),
        booker_id=booking_data['bookerId']
    )


def parse_car(car_data: dict) -> Car:
    return Car(
        id=car_data['id'],
        make=car_data['make'],
        model=car_data['model'],
        color=car_data['color']
    )
