from fastapi import APIRouter

from models.car import Car

router = APIRouter()


@router.get('/cars/', response_model=list[Car])
def get_cars(available: bool = None):
    return []