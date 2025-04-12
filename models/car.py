from datetime import date

from pydantic import BaseModel

from models.booking import Booking


class Car(BaseModel):
    id: str
    make: str
    model: str
    color: str
    bookings: list[Booking]

    def is_available_on(self, rental_date: date) -> bool:
        return not any(booking.is_active_on(rental_date) for booking in self.bookings)