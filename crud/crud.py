import json
from datetime import date, datetime

from models.booking import Booking
from models.car import Car

DB_PATH = 'test_data/cars.json'

def get_all_cars() -> list[Car]:
    with open(DB_PATH, 'r') as file:
        data = json.load(file)

    return [parse_car(car) for car in data.get('cars')]


def get_all_available_cars(rental_date: date) -> list[Car]:
    return [car for car in get_all_cars() if car.is_available_on(rental_date)]


def parse_date(date_str: str) -> date:
    return datetime.strptime(date_str, '%d-%m-%Y').date()


def parse_booking(booking_data: dict) -> Booking:
    return Booking(
        id=booking_data['id'],
        start_date=parse_date(booking_data['startDate']),
        end_date=parse_date(booking_data['endDate']),
        booker_id=booking_data['bookerId']
    )

def parse_car(car_data: dict) -> Car:
    bookings = []

    if car_bookings := car_data.get('bookings'):
        bookings = [parse_booking(booking) for booking in car_bookings]

    return Car(
        id=car_data['id'],
        make=car_data['make'],
        model=car_data['model'],
        color=car_data['color'],
        bookings=bookings,
    )