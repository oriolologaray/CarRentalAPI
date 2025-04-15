from datetime import date

from pydantic import BaseModel, Field


class Booking(BaseModel):
    id: str | None = None
    car_id: str = Field(alias='carId')
    start_date: date = Field(alias='startDate')
    end_date: date = Field(alias='endDate')
    booker_id: str = Field(alias='bookerId')

    def is_active_on(self, rental_date: date) -> bool:
        return self.start_date <= rental_date <= self.end_date
