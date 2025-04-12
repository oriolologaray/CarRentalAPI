from datetime import date

from pydantic import BaseModel


class Booking(BaseModel):
    id: str
    start_date: date
    end_date: date
    booker_id: str

    def is_active_on(self, rental_date: date) -> bool:
        return self.start_date <= rental_date <= self.end_date