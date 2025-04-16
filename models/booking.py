from datetime import date

from pydantic import BaseModel, Field


class Booking(BaseModel):
    id: str | None = None
    car_id: str = Field(alias='carId')
    start_date: date = Field(alias='startDate')
    end_date: date = Field(alias='endDate')
    booker_id: str = Field(alias='bookerId')

    def is_active_on(self, rental_date: date, end_rental_date: date = None) -> bool:
        # If end_rental_date is passed as a parameter, the function will check if there is overlap between ranges.
        if end_rental_date:
            return max(self.start_date, rental_date) <= min(self.end_date, end_rental_date)

        # Else check that the booking is not active for that single day.
        return self.start_date <= rental_date <= self.end_date
