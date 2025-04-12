from datetime import date

from fastapi import APIRouter

from crud.crud import get_all_cars, get_all_available_cars
from models.car import Car

router = APIRouter()


@router.get('/cars/')
def get_cars() -> list[Car]:
    return get_all_cars()


@router.get('/cars/available')
def get_available_cars(rental_date: date = date.today()) -> list[Car]:
    return get_all_available_cars(rental_date)