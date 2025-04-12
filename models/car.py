from pydantic import BaseModel

from models.booking import Booking


class Car(BaseModel):
    id: str
    make: str
    model: str
    color: str
    bookings: list[Booking]

    def is_available(self):
        return not any(booking.is_active() for booking in self.bookings)