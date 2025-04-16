from datetime import date

from fastapi import APIRouter

from app.crud.crud import get_all_cars, get_all_bookings
from app.models.car import Car
from app.utils.logger import logger

router = APIRouter()


@router.get('/cars/')
def get_cars() -> list[Car]:
    logger.info('Attempting to get all cars.')

    return get_all_cars()


@router.get('/cars/available')
def get_available_cars(rental_date: date = date.today()) -> list[Car]:
    logger.info(f'Attempting to get all available cars for date {rental_date}.')

    available_car_ids = [booking.car_id for booking in get_all_bookings() if booking.is_active_on(rental_date)]

    return [car for car in get_all_cars() if car.id in available_car_ids]
