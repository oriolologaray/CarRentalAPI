import json

from pydantic.v1.json import pydantic_encoder

from models.booking import Booking
from models.car import Car
from utils.parsers import parse_car

CARS_DB_PATH = 'test_data/cars.json'
BOOKINGS_DB_PATH = 'test_data/bookings.json'


def get_all_cars() -> list[Car]:
    with open(CARS_DB_PATH, 'r') as file:
        data = json.load(file)

    return [parse_car(car) for car in data]


def get_all_bookings() -> list[Booking]:
    with open(BOOKINGS_DB_PATH, 'r') as file:
        data = json.load(file)

    return [Booking(**booking) for booking in data]


def write_booking(booking: Booking):
    bookings = get_all_bookings() + [booking]

    with open(BOOKINGS_DB_PATH, 'w') as file:
        json.dump([booking.model_dump(by_alias=True) for booking in bookings], file, default=pydantic_encoder, indent=2)
