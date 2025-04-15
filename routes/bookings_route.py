from fastapi import APIRouter

from crud.crud import get_all_bookings, write_booking
from models.booking import Booking
from utils.utils import get_new_booking_id

router = APIRouter()


@router.get('/bookings/')
def get_bookings() -> list[Booking]:
    return get_all_bookings()


@router.post('/bookings/')
def create_booking(booking: Booking) -> Booking:
    booking.id = get_new_booking_id()

    # Check that car is not booked

    write_booking(booking)

    return booking
