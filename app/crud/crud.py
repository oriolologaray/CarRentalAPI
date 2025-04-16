import json

from pydantic.v1.json import pydantic_encoder

from app.config import CARS_DB_PATH, BOOKINGS_DB_PATH
from app.models.booking import Booking
from app.models.car import Car


def get_all_cars() -> list[Car]:
    with open(CARS_DB_PATH, 'r') as file:
        data = json.load(file)

    return [Car(**car) for car in data]


def get_all_bookings() -> list[Booking]:
    with open(BOOKINGS_DB_PATH, 'r') as file:
        data = json.load(file)

    return [Booking(**booking) for booking in data]


def write_booking(booking: Booking):
    bookings = get_all_bookings() + [booking]

    with open(BOOKINGS_DB_PATH, 'w') as file:
        json.dump([booking.model_dump(by_alias=True) for booking in bookings], file, default=pydantic_encoder, indent=2)
