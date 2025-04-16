from fastapi import APIRouter, HTTPException

from app.crud.crud import get_all_bookings, write_booking, get_all_cars
from app.models.booking import Booking
from app.utils.logger import logger
from app.utils.utils import get_new_booking_id

router = APIRouter()


@router.get('/bookings/')
def get_bookings() -> list[Booking]:
    logger.info('Attempting to get all bookings.')

    return get_all_bookings()


@router.post('/bookings/')
def create_booking(new_booking: Booking) -> Booking:
    logger.info('Attempting to create a new booking.')

    car_ids = [car.id for car in get_all_cars()]

    if new_booking.car_id not in car_ids:
        logger.error(f'Car with id {new_booking.car_id} not found.')
        raise HTTPException(status_code=500, detail='Booking creation failed.')

    car_bookings = [booking for booking in get_all_bookings() if booking.car_id == new_booking.car_id]

    if any(booking.is_active_on(new_booking.start_date, new_booking.end_date) for booking in car_bookings):
        logger.error(f'Car with id {new_booking.car_id} is booked on the selected time range.')
        raise HTTPException(status_code=500, detail='Booking creation failed.')

    new_booking.id = get_new_booking_id()
    write_booking(new_booking)

    logger.info(f'Booking with id {new_booking.id} successfully created.')

    return new_booking
